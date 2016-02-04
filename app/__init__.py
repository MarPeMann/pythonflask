from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#define the configure file of the application
app.config.from_object('config')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from blueprint.ud.ud_blueprint import ud
#from blueprint.auth.auth import auth
#Register all needed blueprints
app.register_blueprint(ud)
#app.register_blueprint(login)
from app import routers