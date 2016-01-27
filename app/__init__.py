from flask import Flask

app = Flask(__name__)
#define the configure file of the application
app.config.from_object('config')
from app import routers