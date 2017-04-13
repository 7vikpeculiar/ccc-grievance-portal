from flask_sqlalchemy import SQLAlchemy
from app import db

class Dog(db.Model):
    __tablename__= 'doggies'
    name  = db.Column(db.String(40),primary_key = True)
    describe = db.Column(db.String(200))
    location = db.Column(db.String(200))
    def __init__(self,name,location):
        self.name = name
        self.describe = describe
        self.location = location
    def __repr__(self):
        return "<Dog %r>" % self.name

    def obj(self):
        return {'name': self.name,
                'describe' : self.describe,
                'location' : self.location
                }
