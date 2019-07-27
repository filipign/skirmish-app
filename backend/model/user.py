import datetime

import bcrypt
import jwt

from backend import db
from backend import secret_key


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
        '''
        Generates the Auth Token.

        Returns:
            String: auth token.
        '''
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': self.id
        }
        return jwt.encode(
            payload,
            secret_key,
            algorithm='HS256'
        )

    @staticmethod
    def get_hashed_password(password):
        '''
        Based on plain text password generates salted hash.

        Args:
            password (string): plain text password.
        Returns:
            string: salted hash.
        '''
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    @staticmethod
    def check_password(password, hashed_password):
        '''
        Check if password match hash.

        Args:
            password (string): plain text password.
            hashed_password (string): salted hash of password.
        Returns:
            string: True if generated hash match hashed_password, false otherwise.
        '''
        return bcrypt.checkpw(password.encode('utf8'), hashed_password.encode('utf8'))

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token

        Args:
            auth_token (string): auth_token

        Returns:
        """
        try:
            payload = jwt.decode(auth_token, secret_key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'