from flask import Blueprint, session, redirect
from app.forms import FriendsForm
from app import db

#Create blueprint
#first argument is the name of the blueprint folder
#second is always __name__ attribute
#third param tells the containing folder of your templates
ud = Blueprint('ud',__name__,template_folder='templates',url_prefix=('/app/'))

#/app/delete
@ud.route('delete/<int:id>')
def delete(id):
	return "Delete"

@ud.route('update')
def update():
	return "Update"

@ud.route('addFriends',methods=['GET','POST'])
def addFriend():
	friform = FriendsForm()
	
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
			return render_template('app/templates/template_user.html',isLogged=True,friends=user.friends)
		else:
			flash('All fields are required')
			return render_template('template_add_friends.html',form=friform)

def before_request():
	if not 'isLogged' in session:
		return redirect('/')

ud.before_request(before_request)