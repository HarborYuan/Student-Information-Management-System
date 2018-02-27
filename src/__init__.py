from flask import Flask,render_template

APP = Flask(__name__, instance_relative_config=True)
APP.config.from_object('config')

@APP.route('/')
def index():
    return render_template('index/index.html')

@APP.route('/login/')
def login():
    return render_template('login/login.html')