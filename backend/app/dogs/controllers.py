from flask import Blueprint, request, render_template, make_response\
                  ,flash,jsonify, g, session, redirect, url_for
from app import db
from app.dogs.models import Dog
from app.maps.models import Map
mod_dog = Blueprint('doggies', __name__)

@mod_dog.route('/addDog', methods=['POST'])
def addDog():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['dlocation'] :#or not request.form['describe']:
            return make_response('error: Enter the field names correctly', 400, None)
        try:
            dog = Dog(request.form['name'], request.form['dlocation']) #,request.form['descibe'])
            db.session.add(dog)
            db.session.commit()
            return make_response('success: Created a Dog', 200, None)
        except:
            return make_response('error: Enter the field values correctly', 400, None)

    return None

@mod_dog.route('/dogs', methods=['GET'])
def get_Dog():
    out = Dog.query.all()
    fin = {'dogs' : [ele.obj() for ele in out]}
    return jsonify(fin)

    
@mod_dog.route('/deleteDog',methods=['POST'])
def delete_dog():
	if request.method=='POST':
		if request.form['name']:
			db.session.delete(Dog.query.filter_by(name=request.form['name']).first())
			maps = Map.query.filter_by(name=request.form['name']).all()
                        for m in maps:
				db.session.delete(m)
			db.session.commit()
			return make_response('success:deleted complain',200,None)
		else:
			return make_response('error:enter fields properly',400,None)

	return None

    

    
