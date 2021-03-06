from flask import render_template, Blueprint
from UgniusR.api import public as api
import json

main_bp = Blueprint('main', __name__, template_folder='templates')


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/coursework')
def coursework():
    r = api.courses()
    if r.status_code == 200:
        courses = json.loads(r.data)
        return render_template('coursework.html', heading='Coursework', courses=courses)
    else:
        return render_template('coursework.html'), 404


@main_bp.route('/experience')
def experience():
    return render_template('experience.html', heading='Experience')


@main_bp.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404


@main_bp.errorhandler(500)
def internal(error):
    return render_template('error/500.html'), 500
