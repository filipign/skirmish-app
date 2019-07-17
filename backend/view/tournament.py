from datetime import datetime
import uuid

from flask import Blueprint, request, jsonify, abort, Response

from backend.model.tournament import Tournament
from backend.model.participant import Participant
from backend import db

blueprint = Blueprint('tournament', __name__)


@blueprint.route('/tournament', methods=('POST',))
def create_tournament():
    '''Creates tournament'''
    name = request.json['name']
    tournament_uuid = uuid.uuid4()
    db.session.add(Tournament(name=name, date=datetime.now(), uuid=tournament_uuid))
    db.session.commit()
    return jsonify({'msg': 'Successfully created'})
