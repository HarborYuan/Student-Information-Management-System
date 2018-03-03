from flask import Blueprint, request

API = Blueprint('api', __name__)


@API.route('/login/', methods=['POST'])
def api_login():
    data = request.form.to_dict()
    username = data['username']
    password = data['password']
    if (username == 'asd' and password == '123'):
        return "T"
    else:
        return "F"
