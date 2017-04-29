from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
	__tablename__ = 'user'
	name=db.Column(db.String(40))
	email=db.Column(db.String(40),unique=True)
	username=db.Column(db.String(40),unique=True,primary_key=True)
        password = db.Column(db.String(20))		
        callghmc = db.Column(db.Boolean)
	is_admin = db.Column(db.Boolean)
        def __init__(self, name,email,username,password):
        	self.name=name
		self.email=email
                self.username=username
		self.password = generate_password_hash(password)
                self.callghmc = False
                self.is_admin= True
                 
        def check_password(self, password):
                return check_password_hash(self.password, password)

	def __repr__(self):
		"<username: %r>" %self.username

	def serialize(self):
            return {'name': self.name,'email': self.email,'username': self.username ,'password': self.password,'admin' : self.is_admin}
