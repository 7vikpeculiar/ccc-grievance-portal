from flask import *
from app import db
from app.dogs.models import Dog
from app.complains.models import Complain
from app.maps.models import Map

mod_maps= Blueprint('maps', __name__)

@mod_complain.route('/addmap',methods=['POST'])
def addMap():
	if request.method='POST':
		cname=request.form('cname')
		dname=request.form('dname')
		try:
			if not cname or not dname
				make_response('error: all fields are required')
			newmap=Map(cname,dname)
			db.session.add(newmap)
			db.session.commit()
			return make_response('success:success',200,None)
		except:
	 		return make_response('error:cannot be mapped',400,None)

