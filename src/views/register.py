from flask import Blueprint, render_template
from ..model.common import getMajorList

REGISTER = Blueprint('REGISTER', __name__)


@REGISTER.route('/')
def register():
    majors = getMajorList()
    return render_template(
        'register/register.html', majors=majors, is_login=False)
