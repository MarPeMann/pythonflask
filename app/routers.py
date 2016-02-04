from app import app
#render_template provides access to jinja2 template engine
from flask import render_template,request,make_response,flash,redirect,session
from app.forms import LoginForm
from app.forms import RegisterForm
from app.forms import FriendsForm
from app.db_models import Users,Friends
#from app.db_models import Friends
from app import db
from flask.ext.bcrypt import check_password_hash

@app.route('/',methods=['GET','POST'])
def index():
	login = LoginForm()
	#check if get method
	if request.method == 'GET':
		return render_template('template_index.html',form=login,isLogged=False)
	else:
		#check if form data is valid
		if login.validate_on_submit():
			#check if correct credentials
			user = Users.query.filter_by(email=login.email.data)
			if user.count() == 1 and (check_password_hash(user[0].passw,login.passw.data)):
				session['user_id'] = user[0].id
				session['isLogged'] = True
				# 1 tapa:
				friends = Friends.query.filter_by(user_id=user[0].id)
				print(friends)
				return render_template('template_user.html',isLogged=True,friends=friends)
			else:
				flash('Wrong username or password')
				return render_template('template_index.html',form=login,isLogged=False)
		#form data was not valid
		else:
			flash('Incorrect credentials')
			return render_template('template_index.html',form=login,isLogged=False)


@app.route('/user/<name>')
def user(name):
	print(request.headers.get('User-Agent'))
	return render_template('template_user.html',name=name,isLogged=True)


@app.route('/user',methods=['GET','POST'])
def userParams():
	name = request.args.get('name')
	return render_template('template_user.html',name=name,isLogged=True)

@app.route('/register',methods=['GET','POST'])
def registerUser():
	form = RegisterForm()
	if request.method == 'GET':
		return render_template('template_register.html',form=form, isLogged=False)
	else:
		if form.validate_on_submit():
			user = Users(form.email.data, form.passw.data)
			try:
				db.session.add(user)
				db.session.commit()
			except:
				db.session.rollback()
				flash("Username already in use")
				return render_template('template_register.html',form=form,isLogged=False)
			flash("Name {0} registered.".format(form.email.data))
			return redirect('/')
		else:
			flash('Fill in the required fields')
			return render_template('template_register.html',form=form,isLogged=False)

@app.route('/addFriends',methods=['GET','POST'])
def addFriend():
	friform = FriendsForm()
	if not('isLogged' in session) or (session['isLogged'] == False): 
		return redirect('/')


	if request.method == 'GET':
		return render_template('template_add_friends.html',form=friform,isLogged=True)
	else:
		if friform.validate_on_submit():
			temp = Friends(friform.name.data,friform.address.data,friform.age.data,session['user_id'])
			db.session.add(temp)
			db.session.commit()
			# 2 tapa
			user = Users.query.get(session['user_id'])
			print(user.friends)
			return render_template('template_user.html',isLogged=True,friends=user.friends)
		else:
			flash('All fields are required')
			return render_template('template_add_friends.html',form=friform)

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')



