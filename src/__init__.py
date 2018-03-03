from flask import Flask
from .views.index import INDEX
from .views.login import LOGIN
from .views.api import API

APP = Flask(__name__, instance_relative_config=True)
APP.config.from_object('config')

APP.register_blueprint(INDEX, url_prefix='/')
APP.register_blueprint(LOGIN, url_prefix='/login')
APP.register_blueprint(API, url_prefix='/api')
