from flask_sqlalchemy import *
from flask import *
from app import db
#from app.users.models import User

class Complain(db.Model):
	__tablename__='Complain'
	id=db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_email=db.Column(db.String(40), db.ForeignKey('user.email'))
	description=db.Column(db.String(500), nullable=False)
	name=db.Column(db.String(40), unique=True)#title_of_complain
	done=db.Column(db.String(100), default='no comments for this post')
	
	def __init__(self,user_email,description,name):
		self.user_email=user_email
		self.name=name
		self.description=description
	def __repr__(self):
		"<complainby: %r>"%self.email
	def serialize(self):
		return {'email': self.email,
			'name': self.name,
			'description': self.description,
			'done':self.done
		}



