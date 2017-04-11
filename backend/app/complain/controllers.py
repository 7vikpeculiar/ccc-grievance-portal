from flask import *
from app import db
from app.complain.models import Complain
from app.maps.models import Map
mod_complain = Blueprint('complain', __name__)


@mod_complain.route('/addcomplain',methods=['POST'])
def addComplain():
    if request.method=='POST':
        username=request.form('username')
	description=request.form('description')
	name=request.form('name')
	try:
            if not username or not description or not name:
                return make_response('error:all fields are required',400,None)
	    newcomplain=Complain(username,name,description)
	    db.session.add(newcomplain)
	    db.session.commit()
            return make_response('success: created a complain',200,None)
	except:
            return make_response('error: complain cannot be create',400,None)

			

@mod_complain.route('/complains',methods=['GET'])
def get_Complain():
	out=Complain.query.all()
	fin={'complains' : [ele.obj() for ele in out]}
	return jsonify(fin)



@mod_complain.route('/deletecomplain',methods=['POST'])
def delete_complain():
	if request.method=='POST':
		if request.form['name']:
			db.session.delete(Complain.query.filter_by(name=request.form['name']).first())
			maps = Map.query.filter_by(name=request.form['name']).all()
                        for m in maps:
				db.session.delete(m)
			db.session.commit()
			return make_response('success:deleted complain',200,None)
		else:
			return make_response('error:enter fields properly',400,None)

	return None		



