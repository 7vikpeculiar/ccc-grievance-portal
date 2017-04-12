# Import flask and template operators
from flask import Flask, render_template
from functools import wraps

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
    return render_template('index.html'), 404

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify(message="Unauthorized", success=False), 401
        return f(*args, **kwargs)
    return decorated

# Import a module / component using its blueprint handler variable (mod_auth)
from app.dogs.controllers import mod_dog
from app.users.controllers import mod_users
from app.complains.controllers import mod_complains
from app.maps.controllers import mod_maps

# Register blueprint(s)
app.register_blueprint(mod_dog)
app.register_blueprint(mod_users)
app.register_blueprint(mod_complains)
app.register_blueprint(mod_maps)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
