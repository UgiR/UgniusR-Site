from flask import render_template, Blueprint
from UgniusR.api import public as api
import json

projects_bp = Blueprint('projects', __name__, url_prefix='/projects', template_folder='templates',
                        static_folder='static')


@projects_bp.route('/')
def projects():
    r = api.projects()
    if r.status_code == 200:
        projects = json.loads(r.data)
        return render_template('projects.html', heading='Projects', projects=projects)
    else:
        return render_template('coursework.html'), 404


@projects_bp.route('/this')
def flask_ugniusr():
    return render_template('flask_ugniusr.html', heading='Ugnius R. (Flask)')
