import datetime

import bcrypt
import jwt

from backend import db
from backend import secret_key
from backend import c
from backend.model.blacklist import TokenBlacklist


class User(db.Model):
    '''Represents user managing tournaments.'''
    __tablename__ = '_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(512))
    admin = db.Column(db.Boolean)
    date_created = db.Column(db.Date)

    def __init__(self, login, password, admin=False):
        self.login = login
        self.admin = admin
        # For sake of postgres, password needs to be decoded
        self.password = User.get_hashed_password(password).decode('utf8')
        self.date_created = datetime.datetime.utcnow()

    def encode_auth_token(self):
        '''Generates the Auth Token with user id payload.

        Returns:
            String: auth token.
        '''
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=c.config['jwt']['length_days']),
            'iat': datetime.datetime.utcnow(),
            'sub': self.id
        }
        return jwt.encode(
            payload,
            secret_key,
            algorithm=c.config['jwt']['algorithm']
        )

    @staticmethod
    def get_hashed_password(password):
        '''Based on plain text password generates salted hash.

        Args:
            password (string): plain text password.
        Returns:
            string: salted hash.
        '''
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    @staticmethod
    def check_password(password, hashed_password):
        '''Check if password match hash.

        Args:
            password (string): plain text password.
            hashed_password (string): salted hash of password.
        Returns:
            string: True if generated hash match hashed_password, false otherwise.
        '''
        return bcrypt.checkpw(password.encode('utf8'), hashed_password.encode('utf8'))


    @staticmethod
    def is_token_valid(headers):
        '''Check if token is valid.

        Token validation in based on blacklist and PyJWT decode rules.

        Args:
            headers (dict): Headers of http request.

        Returns:
            integer: Returns user id from token or 0 if token is invalid.
                (as users ids starts from 1)
        '''
        token = headers.get('token')
        if not isinstance(token, str):
            return 0
        blacklisted = TokenBlacklist.query.filter_by(token=token).first()
        if blacklisted:
            return 0
        token_data = { }

        try:
            token_data = jwt.decode(token, secret_key, algorithms=c.config['jwt']['algorithm'])
        except jwt.ExpiredSignatureError:
            return 0
        except jwt.InvalidTokenError:
            return 0

        if not token_data:
            return 0
        return token_data['sub']