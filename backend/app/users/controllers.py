from flask import * 
from app import db

from app.users.models import User
from app.maps.models import Map
from app.complain.models import Complain
from app.maps.models import Map
mod_users = Blueprint('users', __name__)

@mod_users.route('/addUser', methods=['POST'])
def add_user():
	if request.method=='POST':
		name=request.form['name']
		email=request.form['email']
		username=request.form['username']
                print name
                print email
                print username
		try:
			if not name  or not email or not username:
				print '3'
                                return make_response('error: all fields are required',400,None)
			user=User(name,email,username)
			db.session.add(user)
			db.session.commit()
			print '2'
                        return make_response('success: Created a user',200, None)
		except:
			return make_response('error: Enter the field value corectly',400, None)
	print '1'
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
		
		
