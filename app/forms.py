from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email

class LoginForm(Form):
	email = StringField('Enter email',validators=[Required(),Email()])
	passw = PasswordField('Enter password',validators=[Required()])
	submit = SubmitField('Login')
