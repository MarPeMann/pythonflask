from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField,IntegerField,FileField
from wtforms.validators import Required, Email, NumberRange

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
	address = StringField('Address',validators=[Required()])
	age = IntegerField('Age',validators=[Required(),NumberRange(min=0,max=115)])
	upload_file = FileField('Upload image',)
	submit = SubmitField('Add')