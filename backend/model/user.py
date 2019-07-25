import datetime

import bcrypt
import jwt

from backend import db
from backend import secret_key


class User(db.Model):
    __tablename__ = '_user'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64))
    password = db.Column(db.String(512))
    admin = db.Column(db.Boolean)

    def __init__(self, login, password, admin=False):
        self.login = login
        self.admin = admin
        # For sake of postgres, password needs to be decoded
        self.password = User.get_hashed_password(password).decode('utf8')

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token.

        Returns:
            String: auth token.
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                secret_key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def get_hashed_password(password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    @staticmethod
    def check_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf8'), hashed_password.encode('utf8'))

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        """
        try:
            payload = jwt.decode(auth_token, secret_key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'