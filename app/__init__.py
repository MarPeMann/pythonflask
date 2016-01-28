from flask import Flask
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
#define the configure file of the application
app.config.from_object('config')
bootstrap = Bootstrap(app)
from app import routers