from datetime import datetime
import uuid
from json import dumps

from flask import Blueprint, request, jsonify, abort, Response

from backend.model.tournament import Tournament
from backend.model.participant import Participant
from backend import db

blueprint = Blueprint('tournament', __name__)


@blueprint.route('/tournament', methods=('POST', 'GET'))
def manage_tournament():
    '''Creates tournament or get summary info of all tournaments'''
    if request.method == 'POST':
        name = request.json['name']
        tournament_uuid = uuid.uuid4()
        db.session.add(Tournament(name=name, date=datetime.now(), uuid=tournament_uuid))
        db.session.commit()
        return jsonify({'msg': 'Successfully created'})

    if request.method == 'GET':
        tournaments = Tournament.query.all()

        result = []
        for t in tournaments:
            participants = Participant.query.filter_by(tournament_id = t.id).all()
            result.append({
                'name': t.name,
                'date': t.date,
                'uuid': t.uuid,
                'participants': len(participants)
            })
        return jsonify(result)

@blueprint.route('/tournament/<string:uuid>', methods=('GET',))
def get_tournament(uuid):
    '''Get info about single tournament'''
    tournament = Tournament.query.filter_by(uuid = uuid).first()
    if not tournament:
        abort(Response(dumps({'msg': "Torunament doesn't exist"}), 404))

    participants = Participant.query.filter_by(tournament_id = tournament.id).all()
    participants_list = [p.id for p in participants]
    result = {
        tournament.name: {
            'date': tournament.date,
            'uuid': tournament.uuid,
            'participants': participants_list
        }
    }
    print(result)
    return jsonify(result)
