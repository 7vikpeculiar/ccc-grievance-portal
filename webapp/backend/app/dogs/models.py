from flask_sqlalchemy import SQLAlchemy
from app import db

class Dog(db.Model):
    __tablename__= 'Dog'
    name  = db.Column(db.String(40),primary_key = True)
    describe = db.Column(db.String(200),nullable=False)
    location = db.Column(db.String(200))
    accepted = db.Column(db.String(2))
    def __init__(self,name,location,describe):
        self.name = name
        self.describe = describe
        self.location = location
        self.accepted = 'F'
    def __repr__(self):
        return "<Dog %r>" % self.name

    def obj(self):
        return {'name': self.name,
                'describe' : self.describe,
                'location' : self.location,
                'accepted' : self.accepted, 
                }
