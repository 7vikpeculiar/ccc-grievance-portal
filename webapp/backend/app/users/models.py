from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
	__tablename__ = 'user'
	name=db.Column(db.String(40))
	email=db.Column(db.String(40),unique=True,primary_key=True)
        password = db.Column(db.String(20))
	role=db.Column(db.String(10))
	

	def __init__(self, name,email,password,role):
        	self.name=name
		self.email=email
		self.password = generate_password_hash(password)
		self.role=role
        def check_password(self, password):
                return check_password_hash(self.password, password)

	def __repr__(self):
		"<username: %r>" %self.username

	def serialize(self):
		return {'name': self.name,'email': self.email,'role': self.role}

