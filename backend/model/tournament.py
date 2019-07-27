from backend import db
from backend.model.user import User

class Tournament(db.Model):
    '''Represents tournament parring'''
    __tablename__ = 'tournament'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Tournament = db.Column(db.ForeignKey(User.id), nullable=False)
    name = db.Column(db.String(64), index=True)
    date = db.Column(db.Date)
    uuid = db.Column(db.String(36))
    active = db.Column(db.Boolean)
