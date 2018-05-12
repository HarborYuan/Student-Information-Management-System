from flask import Blueprint, render_template

LOGIN = Blueprint('login', __name__)


@LOGIN.route('/')
def login():
    return render_template('login/login.html', is_login=False)
