# Import flask and template operators
from flask import Flask, render_template,redirect,session, jsonify

from functools import wraps
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Define the WSGI application object
app = Flask(__name__)


# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling

@app.errorhandler(404)
def not_found(error):
    print 'Redirecting'
    return redirect('http://127.0.0.1:5050/login')

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
<<<<<<< HEAD
        if 'user_name' not in session:
            return jsonify(message='Unauthorized', success=False), 401
        return f(*args, **kwargs)
    return decorated

def requires_admin_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session and 'role' not in session:
=======
        if 'user_email' not in session:
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
            return jsonify(message="Unauthorized", success=False), 401
        if session['role'] != 'false':
            return jsonify(message="Unauthorized admin needed", success=False), 401
        return f(*args, **kwargs)
    return decorated

<<<<<<< HEAD

=======
def requires_admn_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_email' not in session:
	    return jsonify(message="Unauthorized", success=False), 401
	if session['user_role']!='admin':
	    return jsonify(message="Unauthorized", success=False), 401
	return f(*args, **kwargs)
    return decorated
	
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
# Import a module / component using its blueprint handler variable (mod_auth)
from app.dogs.controllers import mod_dog
from app.users.controllers import mod_users
from app.complains.controllers import mod_complains
#from app.maps.controllers import mod_maps

# Register blueprint(s)
app.register_blueprint(mod_dog)
app.register_blueprint(mod_users)
app.register_blueprint(mod_complains)
#app.register_blueprint(mod_maps)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
