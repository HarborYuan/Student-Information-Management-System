from flask import Blueprint, request, url_for, redirect, session
from ..model.common import judgeStudent, userExist
from ..model.match import IsCellphone, IsMail
from ..model.user import insertUser, userlogin
API = Blueprint('api', __name__)


@API.route('/login/', methods=['POST'])
def api_login():
    data = request.form.to_dict()
    username = data['username']
    password = data['password']
    try:
        if (userlogin(username, password)):
            session['user'] = username
        else:
            return "Error"
        return "Login success"
    except KeyError:
        return "No user"
    return "strange error"


@API.route('/logout/')
def api_logout():
    if 'user' in session:
        session.pop('user', None)
    return redirect(url_for('index.index'))


@API.route('/register/', methods=['POST'])
def api_register():
    data = request.form.to_dict()
    if (judgeStudent(data['username'], data['idcard']) == 'pass'):
        pass
    elif (judgeStudent(data['username'], data['idcard']) == 'no such student'):
        return "1"
    elif (judgeStudent(data['username'], data['idcard']) == 'error'):
        return "2"
    if (data['password1'] == data['password2']):
        pass
    else:
        return "3"
    if (len(data['password1']) < 8):
        return "4"
    if (userExist(data['username'])):
        return "5"
    if (data['major'] == ""):
        return "6"
    if (not IsCellphone().iscellphone(data['phone'])):
        return "7"
    if (not IsMail().ismail(data['email'])):
        return "8"
    if (insertUser(data)):
        session['user'] = data['username']
        return "0"
    return "9"
