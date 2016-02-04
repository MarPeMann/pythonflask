from flask import Blueprint, session, redirect
from app.forms import LoginForm, RegisterForm
from app import db

#Create blueprint
#first argument is the name of the blueprint folder
#second is always __name__ attribute
#third param tells the containing folder of your templates
auth = Blueprint('ud',__name__,template_folder='templates',url_prefix=('/app/'))

#/app/delete
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

def before_request():
	if not 'isLogged' in session:
		return redirect('/')

ud.before_request(before_request)