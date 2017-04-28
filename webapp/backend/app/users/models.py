from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
	__tablename__ = 'user'
	name=db.Column(db.String(40))
<<<<<<< HEAD
	email=db.Column(db.String(40),unique=True)
	username=db.Column(db.String(40),unique=True,primary_key=True)
        password = db.Column(db.String(20))		
        callghmc = db.Column(db.Boolean)
	is_admin = db.Column(db.Boolean)
        def __init__(self, name,email,username,password):
=======
	email=db.Column(db.String(40),unique=True,primary_key=True)
        password = db.Column(db.String(20))
	role=db.Column(db.String(10))
	

	def __init__(self, name,email,password,role):
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
        	self.name=name
		self.email=email
		self.password = generate_password_hash(password)
<<<<<<< HEAD
                self.callghmc = False
                self.is_admin= False 
                 
=======
		self.role=role
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
        def check_password(self, password):
                return check_password_hash(self.password, password)

	def __repr__(self):
		"<username: %r>" %self.username

	def serialize(self):
<<<<<<< HEAD
            return {'name': self.name,'email': self.email,'username': self.username ,'password': self.password,'admin' : self.is_admin}
=======
		return {'name': self.name,'email': self.email,'role': self.role}

>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
