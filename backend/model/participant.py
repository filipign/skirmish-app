from backend import db
from backend.model.tournament import Tournament


class Participant(db.Model):
    __tablename__ = 'participant'

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.ForeignKey(Tournament.id), nullable=False)
    name = db.Column(db.String(64), index=True)
    victories = db.Column(db.Integer)
    defeats = db.Column(db.Integer)
    points = db.Column(db.Integer)
    small_points = db.Column(db.Integer)

class Paring(db.Model):
    __tablename__ = 'paring'

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.ForeignKey(Participant.id), nullable=False)
    participant2_id = db.Column(db.ForeignKey(Participant.id), nullable=False)
    tournament_id = db.Column(db.ForeignKey(Tournament.id), nullable=False)
