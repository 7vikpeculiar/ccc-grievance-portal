from flask import * 
from app import db,requires_admn_auth
from sqlalchemy.exc import IntegrityError
from app import requires_auth
from app.users.models import User
from app.complains.models import Complain
mod_users = Blueprint('users', __name__,url_prefix='/api')

@mod_users.route('/login', methods=['GET'])
def check_login():
<<<<<<< HEAD
    if 'user_name' in session:
        user = User.query.filter(User.username == session['user_name']).first()
        return redirect('http://127.0.0.1:5050/home/'+user.username)
    return render_template('index.html')

@mod_users.route('/adminlogin', methods=['GET'])
def check_admin_login():
    if 'user_name' in session :
        if user['role'] == True:
            user = User.query.filter(User.username == session['user_name']).first()
            return redirect('http://127.0.0.1:5050/admin/home')
    return render_template('index.html')
=======
    if 'user_email' in session:
        user = User.query.filter(User.email == session['user_email']).first()
        return jsonify(success=True, user=user.serialize())
    return jsonify(success=False), 401
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810

@mod_users.route('/loginchk', methods=['GET'])
def login():
<<<<<<< HEAD
    if request.method == 'GET': 
        try:
            username = request.args['username']
            password = request.args['password']
        except KeyError as e:
            return jsonify(success=False, message="%s not sent in the request" % e.args), 400
        user = User.query.filter(User.username == username).first()
        if user is None or not user.check_password(password):
            return jsonify(success=False, message="Invalid Credentials"), 400
        session['user_name'] = user.username
        session['role'] = user.is_admin

        #return jsonify(success=True, user=user.serialize())
        return redirect('http://127.0.0.1:5050/home/'+user.username)

@mod_users.route('/adminchk', methods=['GET'])
def admin_login():
    if request.method == 'GET': 
        try:
            username = request.args['username']
            password = request.args['password']
        except KeyError as e:
            return jsonify(success=False, message="%s not sent in the request" % e.args), 400
        user = User.query.filter(User.username == username).first()
        if user is None or not user.check_password(password) or not user.is_admin :
            return jsonify(success=False, message="Invalid Credentia/ls"), 400
        session['user_name'] = user.username
        session['role'] = user.is_admin
        #return jsonify(success=True, user=user.serialize())
        return redirect('http://127.0.0.1:5050/admin/home')

@mod_users.route('/logout', methods=['POST'])
def logout():
        session.pop('user_name')
	session.pop('role')
        return redirect('http://127.0.0.1:5050')

@mod_users.route('/admin/callghmc', methods=['GET'])
def callghmc():
     if request.method == 'GET':
        out = User.query.filter_by(callghmc=True).all()
        fin = [ele.serialize() for ele in out]        
        return render_template('ghmclist.html',comps=fin)

@mod_users.route('/delghmc/<user>', methods=['POST'])
def delete_callghmc(user):
    if request.method=='POST':
        out = User.query.filter_by(username=user).all()
        out[0].callghmc = False 
        db.session.commit()
        return jsonify(success=True)

@mod_users.route('/callghmc/<user>', methods=['POST'])
@requires_auth
def callghmc_user(user):
    if 'user_name' not in session or session['user_name'] != user:
        return redirect('http://127.0.0.1:5050/login')
    if request.method == 'POST':
        out = User.query.filter_by(username=user).all()
        out[0].callghmc = True 
        db.session.commit()
        return redirect('http://127.0.0.1:5050/home/'+user) 

@mod_users.route('/addUser', methods=['POST','GET'])
=======
    try:
        user_email = request.form['user_email']
        password = request.form['password']
	role=request.form['any']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400
    user = User.query.filter(User.email == user_email).first()
    if user is None or not user.check_password(password):
        return jsonify(success=False, message="Invalid Credentials"), 400
    if user.role!=role:
	return jsonify(success=False,message="Invalid Credentials"), 400
    session['user_role']=user.role
    session['user_email'] = user.email
    return jsonify(success=True, user=user.serialize())

@mod_users.route('/logout', methods=['POST'])
def logout():
	session.pop('user_email')
	session.pop('user_role')
	return jsonify(success=True)
@mod_users.route('/register', methods=['POST'])
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
def add_user():
        if request.method =='GET':
                return render_template('register.html')
	elif request.method=='POST':
		try:
<<<<<<< HEAD
			print '1'
                        name=request.form['name']
			email=request.form['email']
			username=request.form['username']
=======
			name=request.form['name']
			user_email=request.form['user_email']
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
			password=request.form['password']
			role='user'
		except KeyError as e:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400
		if '@' not in email:
			return jsonify(success=False, message="Please enter a valid email"), 400
<<<<<<< HEAD
		if not name  or not email or not username or not password:
=======

		if not name  or not email or not password:
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
                	return jsonify(success=False,message="all fields are required"), 400
		try:
			user=User(name,email,password,role)
			db.session.add(user)
			db.session.commit()
		except IntegrityError as e:
			return jsonify(success=False, message="fields already exist"), 400
                #return jsonify(success=True)
                return redirect('http://127.0.0.1:5050/addUser')

<<<<<<< HEAD
@mod_users.route('/deleteUser', methods=['GET','POST'])
def delete_users():
        if 'user_name' not in session:
            return redirect('http://127.0.0.1:5050/login')    
        if session['role'] != True:
            return jsonify(msg='Unauthorized')    
        if request.method == 'GET':
                users =  User.query.filter_by(is_admin=False).all()
                fin = [ele.serialize() for ele in users]
                return render_template('deleteuser.html',comps=fin)
	elif request.method=='POST':
		if request.form['username']:
			print request.form['username']
                        user = User.query.filter_by(username=request.form['username']).first()
                        #complains = Complain.query.filter_by(username=request.form['username']).all()
                        #for ele in complains:
                            #maps = Map.query.filter_by(ele).all()
                                #for m in maps:
                                #	db.session.delete(m)
                        #    db.session.delete(ele)
			try:
                                db.session.delete(user)
				db.session.commit()
                                #return jsonify(success=True, message="successfully deleted")
                                return redirect('http://127.0.0.1:5050/deleteUser')
			except:
				return jsonify(success=False, message="unsuccessfull"), 400
		else:
			return jsonify(success=False, message="enter the name to be deleted"), 400

	

@mod_users.route('/users',methods=['GET'])
def all_users():
        return jsonify({'users': [i.serialize() for i in User.query.all()]})


@mod_users.route('/normals',methods=['GET','POST'])
def all_normals():
    if 'user_name' not in session:
        return redirect('http://127.0.0.1:5050/login')    
    if session['role'] != True:
        return jsonify(msg='Unauthorized')    
    if request.method == 'GET':
        out = [i.serialize() for i in User.query.filter_by(is_admin=False)]
        return render_template('normalusers.html',comps=out)
    
    if request.method=='POST':
	if request.form['username']:
		user = User.query.filter_by(username=request.form['username']).first()
              	try:
			user.is_admin=True
                        db.session.commit()
                        return redirect('http://127.0.0.1:5050/normals')
		except:
			return jsonify(success=False, message="unsuccessfull"), 400
		else:
			return jsonify(success=False, message="enter the name to be deleted"), 400

=======
@mod_users.route('/user/<id>/delete', methods=['POST'])
@requires_admn_auth
def delete_users(id):
	user=User.query.filter(User.email==id).first()
	if user is None:
		return jsonify(success=False), 404
	else:
		db.session.delete(user)
		db.session.commit()
		return jsonify(success=True)
		

	
@mod_users.route('/user',methods=['GET'])
@requires_admn_auth
def all_users():
        return jsonify(users=[i.serialize() for i in User.query.all()])
>>>>>>> ced0be31bd47d46087c9d879b71e5101a6ff4810
		
@mod_users.route('/user/<id>/approve',methods='POST')
@requires_admn_auth
def approve_user(id):
	user=User.query.filter(User.email==id).first()
	if user is None:
		return jsonify(success=False), 404
	else:
	 	user.role='admin'
	 	db.session.commit()
	 	return jsonify(success=True)
	 	
	
