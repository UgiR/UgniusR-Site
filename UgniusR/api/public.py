from flask import Blueprint, Response, jsonify
from sqlalchemy import exc
from sentry_sdk import capture_exception
from UgniusR.api.models import Course

public_api_bp = Blueprint('public_api', __name__, url_prefix='/api/public')


@public_api_bp.route('/courses')
def courses():
    try:
        all_courses = Course.query.all()
    except exc.SQLAlchemyError as e:
        capture_exception(e)
        return Response(status=404)

    content = []
    for course in reversed(all_courses):
        c = {}
        c['Course'] = course.course
        c['Title'] = course.name
        c['Term'] = course.term
        content.append(c)
    return jsonify(content)
