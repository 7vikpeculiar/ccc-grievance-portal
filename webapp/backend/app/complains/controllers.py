from flask import *
from app import *
from app.complains.models import Complain
from app.dogs.models import Dog
mod_complains= Blueprint('complain', __name__,url_prefix='/api')


@mod_complains.route('/addcomplain',methods=['POST'])
@requires_auth
def addComplain():
	if request.method=='POST':
		description=request.form['description']
		name=request.form['name']
		user_email=session['user_email']
		try:
			if not description or not name:
				return jsonify(success=False),404
			newcomplain=Complain(user_email,description,name)
			db.session.add(newcomplain)
	    		db.session.commit()
            		return jsonify(success=True, complain=complain.serialize())
		except:
            		return jsonify(success=False),404

			
@mod_complains.route('/addcomplain',methods=['GET'])
@requires_auth
def addComplain():
        if request.method=='GET':
		out = Dog.query.filter_by(accepted=True).all()
		fin = [ele.obj() for ele in out]
		finee = [ele['name'] for ele in fin]
		return jsonify(success=True,names=finee)

@mod_complains.route('/admn/complains',methods=['GET'])
@requires_admn_auth
def get_all_Complains():
	user_email=session['user_email']
	out=Complain.query.all()
	return jsonify(success=True,complains=[todo.serialize() for todo in out])

@mod_complains.route('/complains',methods=['GET'])
@requires_auth
def get_user_complains():
	user_email=session['user_email']
	out=Complain.query.filter_by(Complain.user_email==user_email)
	return jsonify(success=True,complains=[todo.serialize() for todo in out])
	
@mod_complains.route('/complains/<id>',methods=['GET'])
@requires_auth
def get_complains(id):
	user_email=session['user_email']
	out=Complain.query.filter_by(Complain.id==id,Complain.user_email==user_email).all()
	return jsonify(success=True,complains=[todo.serialize() for todo in out])


@mod_complains.route('/complains/<id>/done', methods=['POST'])
@requires_auth
def mark_done(id):
	user_email= session['user_email']
	complain = Complain.query.filter(Complain.id == id, Complain.user_email == user_email).first()
	if complain is None:
		return jsonify(success=False), 404
	else:
		complain.done = True
		db.session.commit()
		return jsonify(success=True)

@mod_complains.route('/complains/<id>/delete',methods=['POST'])
@requires_auth
def delete_complain(id):
	if request.method=='POST':
		user_email=session['user_email']
		complaint=Complain.query.filter_by(Complain.id == id, Complain.user_email == user_email).first()
		if complaint is None:
			return jsonify(success=False), 404
		else:
			db.session.delete(complaint)
			db.session.commit()
		return jsonify(success=True)
	else:
		return jsonify(success=False), 404		


