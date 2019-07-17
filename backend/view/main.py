from flask import Blueprint, request, jsonify

from backend.model.tournament import Tournament
from backend import db

blueprint = Blueprint('main', __name__)


@blueprint.route('/hi')
def hello():
    return 'hi'
