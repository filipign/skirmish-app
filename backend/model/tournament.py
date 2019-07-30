from datetime import datetime
import uuid

from backend import db
from backend.model.user import User
from backend import c


class Tournament(db.Model):
    '''Represents tournament'''
    __tablename__ = 'tournament'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey(User.id), nullable=False)
    name = db.Column(db.String(64), index=True)
    date = db.Column(db.Date)
    uuid = db.Column(db.String(36))
    active = db.Column(db.Boolean)

    # Config related fields
    rounds = db.Column(db.Integer)
    current_round = db.Column(db.Integer)
    victory_value = db.Column(db.Integer)
    tie_value = db.Column(db.Integer)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

        self.date = datetime.now()
        self.uuid = uuid.uuid4()
        self.active = True
        self.rounds = c.config['tournament']['rounds']
        self.current_round = 1
        self.victory_value = c.config['tournament']['vp']
        self.tie_value = c.config['tournament']['tie']
