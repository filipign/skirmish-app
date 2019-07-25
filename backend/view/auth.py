from json import dumps

from flask import Blueprint, request, jsonify, abort, Response

from backend.model.user import User
from backend import db

blueprint = Blueprint('auth', __name__)


@blueprint.route('/auth/login', methods=('POST',))
def login():
    data = request.get_json()
    user = User.query.filter_by(login=data.get('login')).first()
    print(data.get('password').encode('utf8'))
    print(user.password.encode('utf8'))
    if user:
        return jsonify({'yes': User.check_password(data.get('password'), user.password)})

@blueprint.route('/auth/register', methods=('POST',))
def register():
    data = request.get_json()
    user = User(
        login=data.get('login'),
        password=data.get('password')
    )
    db.session.add(user)
    db.session.commit()

    auth_token = User.encode_auth_token(user.id)
    return auth_token

@blueprint.route('/auth/logout', methods=('POST',))
def logout():
    pass

@blueprint.route('/auth/user', methods=('GET',))
def get_token():
    auth_header = request.headers.get('Authorization')
    auth_token = auth_header.split(" ")[1]
    resp = User.decode_auth_token(auth_token)
    user = User.query.filter_by(id=resp).first()
    return jsonify(user.id)