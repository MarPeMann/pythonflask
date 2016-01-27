from app import app
#render_template provides access to jinja2 template engine
from flask import render_template,request,make_response

@app.route('/')
def index():
	name = 'M M'
	address='Tornipolku'
	response = make_response(render_template('template_index.html'))
	response.headers.add('Cache-Control','no-cache')
	return response
	#return render_template('template_index.html',title=address,name=name)

@app.route('/user/<name>')
def user(name):
	print(request.headers.get('User-Agent'))
	return render_template('template_user.html',name=name)


@app.route('/user',methods=['GET','POST'])
def userParams():
	name = request.args.get('name')
	return render_template('template_user.html',name=name)

