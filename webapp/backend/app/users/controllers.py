from flask import * 
from app import db
from sqlalchemy.exc import IntegrityError

from app.users.models import User
from app.maps.models import Map
from app.complains.models import Complain
mod_users = Blueprint('users', __name__)

@mod_users.route('/login', methods=['GET'])
def check_login():
    if 'user_id' in session:
        user = User.query.filter(User.id == session['user_id']).first()
        return jsonify(success=True, user=user.serialize())
    return jsonify(success=False), 401

@mod_users.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400
    user = User.query.filter(User.email == email).first()
    if user is None or not user.check_password(password):
        return jsonify(success=False, message="Invalid Credentials"), 400
    session['user_id'] = user.id
    return jsonify(success=True, user=user.serialize())


@mod_users.route('/addUser', methods=['POST'])
def add_user():
	if request.method=='POST':
		name=request.form['name']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
                print name
                print email
                print username
                print password
		try:
			if not name  or not email or not username or not password:
                                return make_response('error: all fields are required',400,None)
			user=User(name,email,username,password)
			db.session.add(user)
			db.session.commit()
                        return make_response('success: Created a user',200, None)
		except:
			return make_response('error: Enter the field value corectly',400, None)
        return 'OK'

@mod_users.route('/deleteUser', methods=['POST'])
def delete_users():
	if request.method=='POST':
		if request.form['username']:
			db.session.delete(User.query.filter_by(username=request.form['username']).first())
			complains = Complain.query.filter_by(username=request.form['username']).all()
			for ele in complains:
				maps = Map.query.filter_by(ele).all()
				for m in maps:
					db.session.delete(m)
				db.session.delete(ele)
			db.session.commit()
			return make_response('success:deleted user',200,None)
		else:
			return make_response('error:enter the field names correctly',400,None)

	return None
	



@mod_users.route('/users',methods=['GET'])
def all_users():
        return jsonify({'users': [i.serialize() for i in User.query.all()]})
		
		
