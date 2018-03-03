from flask import Blueprint, render_template

INDEX = Blueprint('index', __name__)


@INDEX.route('/')
def index():
    return render_template('index/index.html')
