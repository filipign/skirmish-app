from json import dumps

from flask import Blueprint, request, jsonify, abort, Response

from backend.model.tournament import Tournament
from backend.model.participant import Participant
from backend import db

blueprint = Blueprint('participant', __name__)


@blueprint.route('/participant', methods=('PUT',))
def add_participants():
    '''Create participants from json.'''
    for participant in request.json.values():
        tournament = Tournament.query.get(participant['tournament_id'])
        if not tournament:
            abort(Response(dumps({'msg': "Torunament doesn't exist"}), 404))

        db.session.add(Participant(**participant))
        db.session.commit()

    return jsonify({'msg': 'Successfully created'})

@blueprint.route('/participant/<int:id>', methods=('DELETE',))
def delete_participant(id):
    '''Delete participants, based on his id.'''
    participant = Participant.query.get(id)
    if not participant:
        abort(Response(dumps({'msg': "Participant doesn't exist"}), 404))

    db.session.delete(participant)
    db.session.commit()
    return jsonify({'msg': 'Successfully deleted'})