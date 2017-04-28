from flask import Blueprint, request, render_template, make_response\
                  ,flash,jsonify, g, session, redirect, url_for
from app import db
from app.dogs.models import Dog
from app.maps.models import Map
mod_dog = Blueprint('Dog', __name__)

@mod_dog.route('/addDog', methods=['POST','GET'])
def addDog():
    if 'user_name' not in session:
        return redirect('http://127.0.0.1:5050/login')
    if request.method == 'GET':
        return render_template('addcanine.html')
    elif request.method == 'POST':
        if not request.form['name'] or not request.form['dlocation'] or not request.form['describe']:
            return render_template('param.html')
        #return make_response('error: Enter the field names correctly', 400, None)
        try:
            newdog = Dog(request.form['name'], request.form['dlocation'],request.form['describe'])
            db.session.add(newdog)
            db.session.commit()
            #return make_response('success: Created a Dog', 200, None)
            return redirect('http://127.0.0.1:5050/addDog')
        except:
            #return make_response('error: Enter the field values correctly', 400, None)
            return render_template('param.html')
        #return redirect('http://127.0.0.1:5050/addDog')

@mod_dog.route('/dogs', methods=['GET'])
def get_Dog():
    out = Dog.query.all()
    fin = {'dogs' : [ele.obj() for ele in out]}
    return jsonify(fin)

@mod_dog.route('/unapprovedDogs', methods=['GET','POST'])
def get_unapproved():
    if 'user_name' not in session:
        return redirect('http://127.0.0.1:5050/login')
    if session['role'] !=True:
        return jsonify(msg='Unauthorized')
    if request.method=='GET':
        out = Dog.query.filter_by(accepted='F').all()
        fin = [ele.obj() for ele in out]
        return render_template('unapproveddogs.html',comps=fin)
    if request.method=='POST':
        if request.form['name']:
            dog=Dog.query.filter_by(name=request.form['name']).first()
#maps = Map.query.filter_by(name=request.form['name']).all()
#                        for m in maps:
            db.session.delete(dog)
            db.session.commit()
            return redirect('http://127.0.0.1:5050/unapprovedDogs')
        else:
            return make_response('error:enter fields properly',400,None)
        return None

@mod_dog.route('/acceptedDogs', methods=['GET'])
def accepted_Dog():
    out = Dog.query.filter_by(accepted='T').all()
    fin = [ele.obj() for ele in out]
    return render_template('getdog.html',comps=fin)

@mod_dog.route('/approveDog', methods=['GET','POST'])
def getaccepteddog():
    if 'user_name' not in session:
        return redirect('http://127.0.0.1:5050/login')
    if session['role'] !=True:
        return jsonify(msg='Unauthorized')
    if request.method == 'GET':
        out = Dog.query.filter_by(accepted='F').all()
        fin = [ele.obj() for ele in out]
        return render_template('approvedog.html',comps=fin)
    if request.method == 'POST':
        out = Dog.query.filter_by(name=request.form['name']).all()
        print out[0].obj()
        out[0].accepted='T'
        db.session.commit()
        return redirect('http://127.0.0.1:5050/approveDog')
 
@mod_dog.route('/deleteDog',methods=['POST','GET'])
def delete_dog():
        if 'user_name' not in session:
            return redirect('http://127.0.0.1:5050/login')
        if session['role'] !=True:
            return jsonify(msg='Unauthorized')
        if request.method == 'GET':
                out = Dog.query.all()
                fin = [ele.obj() for ele in out]
                return render_template('deletedog.html',comps=fin)
        if request.method=='POST':
		if request.form['name']:
			dog=Dog.query.filter_by(name=request.form['name']).first()
#maps = Map.query.filter_by(name=request.form['name']).all()
#                        for m in maps:
                        db.session.delete(dog)
                        db.session.commit()
#                        return make_response('success:deleted complain',200,None)
                        return redirect('http://127.0.0.1:5050/deleteDog')
                        return 
		else:
			return make_response('error:enter fields properly',400,None)

	return None
