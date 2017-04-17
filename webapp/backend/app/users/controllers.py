from flask import * 
from app import db,requires_admn_auth
from sqlalchemy.exc import IntegrityError

from app.users.models import User
from app.complains.models import Complain
mod_users = Blueprint('users', __name__,url_prefix='/api')

@mod_users.route('/login', methods=['GET'])
def check_login():
    if 'user_email' in session:
        user = User.query.filter(User.email == session['user_email']).first()
        return jsonify(success=True, user=user.serialize())
    return jsonify(success=False), 401

@mod_users.route('/login', methods=['POST'])
def login():
    try:
        user_email = request.form['user_email']
        password = request.form['password']
	role=request.form['any']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400
    user = User.query.filter(User.email == user_email).first()
    if user is None or not user.check_password(password):
        return jsonify(success=False, message="Invalid Credentials"), 400
    if user.role!=role:
	return jsonify(success=False,message="Invalid Credentials"), 400
    session['user_role']=user.role
    session['user_email'] = user.email
    return jsonify(success=True, user=user.serialize())

@mod_users.route('/logout', methods=['POST'])
def logout():
	session.pop('user_email')
	session.pop('user_role')
	return jsonify(success=True)
@mod_users.route('/register', methods=['POST'])
def add_user():
	if request.method=='POST':
		try:
			name=request.form['name']
			user_email=request.form['user_email']
			password=request.form['password']
			role='user'
		except KeyError as e:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400
		if '@' not in email:
			return jsonify(success=False, message="Please enter a valid email"), 400

		if not name  or not email or not password:
                	return jsonify(success=False,message="all fields are required"), 400
		try:
			user=User(name,email,password,role)
			db.session.add(user)
			db.session.commit()
                        
		except IntegrityError as e:
			return jsonify(success=False, message="fields already exist"), 400
       		return jsonify(success=True)

@mod_users.route('/user/<id>/delete', methods=['POST'])
@requires_admn_auth
def delete_users(id):
	user=User.query.filter(User.email==id).first()
	if user is None:
		return jsonify(success=False), 404
	else:
		db.session.delete(user)
		db.session.commit()
		return jsonify(success=True)
		

	
@mod_users.route('/user',methods=['GET'])
@requires_admn_auth
def all_users():
        return jsonify(users=[i.serialize() for i in User.query.all()])
		
@mod_users.route('/user/<id>/approve',methods='POST')
@requires_admn_auth
def approve_user(id):
	user=User.query.filter(User.email==id).first()
	if user is None:
		return jsonify(success=False), 404
	else:
	 	user.role='admin'
	 	db.session.commit()
	 	return jsonify(success=True)
	 	
	
