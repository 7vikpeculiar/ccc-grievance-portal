from flask_sqlalchemy import SQLAlchemy
from app import db
from app.complains.models import Complain
from app.dogs.models import Dog

class Map(db.Model):
	__tablename__='Map'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	cname=db.Column(db.String(40),db.ForeignKey('Complain.id'))
	dname=db.Column(db.String(40),db.ForeignKey('Dog.name'))

	def __init__(self,cname,dname):
		self.cname=cname
		self.dname=dname
	def __repr__(self):
		"<complainname: %r>" % self.dname
	def serialize(self):
		return {'complain_name': self.cname,'dog_name': self.dname}
		


