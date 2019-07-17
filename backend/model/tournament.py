from backend import db


class Tournament(db.Model):
    __tablename__ = 'tournament'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    date = db.Column(db.Date)
    uuid = db.Column(db.String(36))
