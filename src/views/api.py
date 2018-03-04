from flask import Blueprint, request, url_for, redirect, session
API = Blueprint('api', __name__)


@API.route('/login/', methods=['POST'])
def api_login():
    data = request.form.to_dict()
    username = data['username']
    password = data['password']
    dict_user = {"testuser": "testpassword"}
    try:
        if (dict_user[username] == password):
            session['user'] = username
        else:
            return "Error"
        return "Login success"
    except KeyError:
        return "No user"
    return "strange error"


@API.route('/logout/')
def api_logout():
    session.pop('user', None)
    return redirect(url_for('index.index'))
