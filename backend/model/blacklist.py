from datetime import datetime

from backend import db

# TODO: Blacklist of tokens is now stored in same database with other data,
# would be good to setup redis db for that.
class TokenBlacklist(db.Model):
    '''Represents blacklisted JWT tokens.'''
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(512), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.now()
