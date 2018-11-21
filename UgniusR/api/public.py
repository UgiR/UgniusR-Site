from flask import Blueprint, Response, jsonify, url_for
import csv
import os
from UgniusR.api import public_api_bp


@public_api_bp.route('/courses')
def courses():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(dir_path + '/resources/coursework.csv', 'r') as file:
            reader = csv.DictReader(file)
            return jsonify(list(reader))
    except IOError as e:
        print(e)
        return Response(status=404)
