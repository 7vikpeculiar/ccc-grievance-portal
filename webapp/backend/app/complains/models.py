from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import db
from app.users.models import User

class Complain(db.Model):
	__tablename__='Complain'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	username=db.Column(db.String(40),db.ForeignKey(User.username))
	description=db.Column(db.String(500),nullable=False)
	name=db.Column(db.String(40),unique=True)   #title_of_complain
	comment=db.relationship('Comment',backref="complain",cascade="all, delete-orphan" ,lazy='dynamic')

	def __init__(self,username,name,description):
		self.username=username
		self.name=name
		self.description=description
	def __repr__(self):
		"<complainby: %r>"%self.username
	def serialize(self):
		return {'username': self.username,'name': self.name,'description': self.description}

class Comment(db.Model):
	__tablename__='Comment'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	username=db.Column(db.String(40))
	content=db.Column(db.String(500),nullable=False)
	complain_id=db.Column(db.Integer,db.ForeignKey('Complain.id'))
	
	def __init__(self,username,content):
		self.username=username
		self.content=content


