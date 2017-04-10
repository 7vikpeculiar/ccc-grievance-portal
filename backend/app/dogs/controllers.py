from flask import Blueprint, request, render_template, make_response\
                  ,flash,jsonify, g, session, redirect, url_for
from app import db
from app.dogs.models import Dog
from app.maps.models import Map
mod_dog = Blueprint('doggies', __name__)

@mod_dog.route('/addDog', methods=['GET'])
def addDog():
    name = request.args.get('name')
    location = request.args.get('location')
    description = request.args.get('describe')
    newDog = Dog(name,location,description)
    if not name or not location or not description:
        return make_response({'error': 'Improper Request'})
    db.session.add(newDog)
    try:
        db.session.commit()
    except:
        return make_response({'success':"Dog got Added"});
    return make_response({'error': 'Dog already exists or enter the field values properly'})

@mod_dog.route('/dogs', methods=['GET'])
def get_Dog():
    out = Dog.query.all()
    fin = {'dogs' : [ele.obj() for ele in out]}
    return jsonify(fin)

    
@mod_dog.routes('/deletecomplain',methods=['POST'])
def delete_complain():
	if request.method=='POST':
		if request.form['name']:
			db.session.delete(Dog.query.filter_by(name=request.form['name']).first())
			maps = Map.query.filter_by(name=request.form['name']).all()
			for m in maps
				db.session.delete(m)
			db.session.commit()
			return make_response('success:deleted complain',200,None)
		else:
			return make_response('error:enter fields properly',400,None)

	return None

    

    
