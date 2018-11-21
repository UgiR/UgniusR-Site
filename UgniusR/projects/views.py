from flask import render_template, Blueprint

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')


@projects_bp.route('/')
def projects():
    return render_template('projects.html', heading='Projects')


@projects_bp.route('/this')
def flask_ugniusr():
    return render_template('flask_ugniusr.html')
