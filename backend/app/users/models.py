from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
	__tablename__ = 'user'
	name=db.Column(db.String(40))
	email=db.Column(db.String(40),unique=True)
	username=db.Column(db.String(40),unique=True,primary_key=True)
		
		

	def __init__(self, name,email,username):
        	self.name=name
		self.email=email
		self.username=username
	def __repr__(self):
		"<username: %r>" %self.username

	def serialize(self):
		return {'name': self.name,'email': self.email,'username': self.username}

