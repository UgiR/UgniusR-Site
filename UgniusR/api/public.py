from flask import Blueprint, Response, jsonify
import csv
import os

public_api_bp = Blueprint('public_api', __name__, url_prefix='/api/public')


@public_api_bp.route('/courses')
def courses():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(dir_path + '/resources/coursework.csv', 'r') as file:
            reader = csv.DictReader(file)
            return jsonify(list(reader))
    except IOError:
        return Response(status=404)