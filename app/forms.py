from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email

class LoginForm(Form):
	email = StringField('Enter email',validators=[Required(),Email()])
	passw = PasswordField('Enter password',validators=[Required()])
	submit = SubmitField('Login')

class RegisterForm(Form):
	email = StringField('Your email',validators=[Required(),Email()])
	passw = PasswordField('Enter password',validators=[Required()])
	submit = SubmitField('Register')

class FriendsForm(Form):
	name = StringField('Name',validators=[Required()])
	age = StringField('Age',validators=[Required()])
	address = StringField('Address',validators=[Required()])
	submit = SubmitField('Add')