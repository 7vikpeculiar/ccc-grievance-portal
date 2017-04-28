from flask import *
from app import db
from app.complains.models import Complain
from sqlalchemy import and_
from app.maps.models import Map
from app.dogs.models import Dog
mod_complains= Blueprint('complain', __name__)
    
@mod_complains.route('/addcomplain/<user>',methods=['POST','GET'])
def addComplain(user):
    if 'user_name' not in session:
        return redirect('http://127.0.0.1:5050/login')
    if session['user_name'] != user:
        return redirect('http://127.0.0.1:5050/login')
    if request.method=='GET':
        out = Dog.query.filter_by(accepted='T').all() 
        fin = [ele.obj() for ele in out]
        return render_template('getdog.html',names=fin,tbox=user)    

    if request.method=='POST':
        username=request.form['username']
	description=request.form['description']
	name=request.form['name']
	try:
            if not username or not description or not name:
                return render_template('param.html')
	    newcomplain=Complain(username,name,description)
	    db.session.add(newcomplain)
            print request.form.get('dogs')
            print newcomplain.id
	    db.session.commit()
            #return make_response('success: created a complain',200,None)
            return redirect('http://127.0.0.1:5050/addcomplain/'+user)
	except:
            return render_template('getdog.html',names=fin,tbox=user)    
        # return make_response('error: complain cannot be created',400,None)

@mod_complains.route('/admin/home',methods=['GET'])
def view_complain():
    if 'user_name' not in session:
        return render_template('index.html')
    if session['role']==True:
        out=Complain.query.all()
	fin=[ele.serialize() for ele in out]
	return render_template('adminhome.html',comps=fin)

@mod_complains.route('/viewcomplains/<user>',methods=['GET'])
def view_user_complain(user):
    if 'user_name' not in session or session['user_name'] != user:
            return redirect('http://127.0.0.1:5050/login')
    #if session['role'] == True:
    #        return redirect('http://127.0.0.1:5050/admin/home')
    out=Complain.query.filter_by(username=user).all()
    fin=[ele.serialize() for ele in out]
    return render_template('usercomplain.html',comps=fin,tbox=user)

@mod_complains.route('/edit/<user>',methods=['GET'])
def user_edit_complain(user):
    if 'user_name' not in session or session['user_name'] != user:
        return redirect('http://127.0.0.1:5050/login')
    if request.method == 'GET':
        out=Complain.query.filter(Complain.username==user).all()
        return render_template('editcomplain.html',comps=out,tbox=user)
    
@mod_complains.route('/editcomplain/<user>',methods=['POST'])
def user_edit_complain_post(user):
    if request.method == 'POST':
        if user:
            out=Complain.query.filter(and_(Complain.username==user,Complain.name==request.form['name'])).all()
            try:
                out[0].description = request.form['description']
                db.session.commit()
                #return make_response('success: edited a complain',200,None)
                return redirect('http://127.0.0.1:5050/edit/'+user)
            except:
                return make_response('error: Couldnot edit the  complain',400,None)
        
@mod_complains.route('/complains',methods=['GET'])
def get_Complain():
	out=Complain.query.all()
	fin={'complains' : [ele.serialize() for ele in out]}
	return jsonify(fin)

@mod_complains.route('/home/<user>',methods=['GET'])
def get_home(user):
    if 'user_name' not in session:
        return jsonify(msg='Please Login first')
    if session['user_name'] != user:
        return jsonify(msg='Unauthorized')
    out=Complain.query.all()
    fin=[ele.serialize() for ele in out]
    return render_template('home.html',comps=fin,tbox=user)
    
@mod_complains.route('/deletecomplain',methods=['POST','GET'])
def delete_complain():
        if 'user_name' not in session:
            return redirect('http://127.0.0.1:5050/login')
        if request.method == 'GET':
                out=Complain.query.all()
                fin=[ele.serialize() for ele in out]
                return render_template('admindel.html',comps=fin)
        if request.method == 'POST':
		if request.form['name']:
			db.session.delete(Complain.query.filter_by(name=request.form['name']).first())
                        #maps = Map.query.filter_by(name=request.form['name']).all()
                        #for m in maps:
                        #	db.session.delete(m)
			db.session.commit()
                        if request.form['user'] == 'anadmink':
                            print 'imhere'
                            return redirect('http://127.0.0.1:5050/admin/home')
                        return redirect('http://127.0.0.1:5050/viewcomplains/'+request.form['user'])
                        #return make_response('success:deleted complain',200,None)
		else:
			return make_response('error:enter fields properly',400,None)		

@mod_complains.route('/admin/deletecomplain',methods=['POST'])
def admin_delete_complain():
        if 'user_name' not in session:
            return redirect('http://127.0.0.1:5050/login')
        if request.method == 'POST':
		if request.form['name']:
			db.session.delete(Complain.query.filter_by(name=request.form['name']).first())
                        db.session.commit()
                        return redirect('http://127.0.0.1:5050/admin/home')
		else:
			return make_response('error:enter fields properly',400,None)		


