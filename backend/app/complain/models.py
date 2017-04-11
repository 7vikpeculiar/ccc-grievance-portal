from flask_sqlalchemy import SQLAlchemy
from app import db
from app.users.models import User

class Complain(db.Model):
	__tablename__='Complain'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	username=db.Column(db.String(40),db.ForeignKey(User.username))
	description=db.Column(db.String(500))
	name=db.Column(db.String(40),unique=True)


	def __init__(self,username,description,name):
		self.username=username
		self.name=name
		self.description=description
	def __repr__(self):
		"<complainby: %r>"%self.username
	def serialize(self):
		return {'username': self.username,'name': self.name,'description': self.description}


