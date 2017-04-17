from flask import *
from app import db
from app.dogs.models import Dog
#from app.maps.models import Map
mod_dog = Blueprint('Dog', __name__)

@mod_dog.route('/dogs', methods=['POST'])
def addDog():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['dlocation'] or not request.form['describe']:
	    return jsonify(success=False), 404
        try:
            newdog = Dog(request.form['name'], request.form['dlocation'],request.form['describe'])
            db.session.add(newdog)
            db.session.commit()
            return jsonify(success=True)
        except:
            return jsonify(success=False), 404

@mod_dog.route('/dogs', methods=['GET'])
def get_Dog():
    out = Dog.query.all()
    fin = {'dogs' : [ele.obj() for ele in out]}
    return jsonify(fin)

@mod_dog.route('/dogs/approved', methods=['GET'])
def accepted_Dog():
    out = Dog.query.filter_by(accepted=True).all()
    fin = {'dogs' : [ele.obj() for ele in out]}
    return jsonify(fin)

    
@mod_dog.route('/dogs/<id>/delete',methods=['POST'])
def delete_dog():
	if request.method=='POST':
		dog=Dog.query.filter_by(Dog.name==id).first()
		db.session.delete(dog)
		db.session.commit()
		return jsonify(success=True)
	else:
		return jsonify(success=False), 404



    

    
