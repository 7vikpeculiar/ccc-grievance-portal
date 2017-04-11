# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.dogs.controllers import mod_dog
from app.users.controllers import mod_users
from app.complain.controllers import mod_complain
from app.maps.controllers import mod_maps
#nikky fill it up
# Register blueprint(s)
app.register_blueprint(mod_dog)
app.register_blueprint(mod_users)
app.register_blueprint(mod_complain)
app.register_blueprint(mod_maps)
#nikky fill it up

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
