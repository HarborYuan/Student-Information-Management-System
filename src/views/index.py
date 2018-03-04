from flask import Blueprint, render_template, session

INDEX = Blueprint('index', __name__)


@INDEX.route('/')
def index():
    if 'user' in session:
        return render_template(
            'index/index.html',
            is_login=True,
            user=session['user'])
    return render_template('index/index.html', is_login=False)
