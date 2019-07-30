from json import dumps

from flask import Blueprint, request, jsonify, abort, Response

from backend.model.tournament import Tournament
from backend.model.participant import Participant
from backend.model.user import User
from backend.model.blacklist import TokenBlacklist
from backend.view.response import ResponseStrings, ResponseMessages
from backend import db

blueprint = Blueprint('tournament', __name__)


@blueprint.route('/tournament', methods=('POST', 'GET'))
def manage_tournament():
    '''Creates tournament or get summary info of all tournaments.

        Post methods expect tournament data.
        Example:
            {
                "name": "Grand Clash",
            }

        Returns:
            201 status code with success message and tournament uuid.
            400 status code if token or name is invalid.
    '''
    if request.method == 'POST':
        user_id = User.is_token_valid(request.headers)
        if not user_id:
            return jsonify(ResponseMessages.INVALID_TOKEN.value), 400

        name = request.json['name']
        if not isinstance(name, str):
            return jsonify({
                ResponseStrings.STATUS.value: ResponseStrings.FAILED.value,
                ResponseStrings.MESSAGE.value: "Invalid name"
            }), 400
        tournament = Tournament(
            name=name,
            user_id=user_id,
        )
        db.session.add(tournament)
        db.session.commit()

        return jsonify({
            ResponseStrings.STATUS.value: ResponseStrings.SUCCESS.value,
            'uuid': tournament.uuid,
        }), 201

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
    return jsonify(result)
