from json import dumps

from flask import Blueprint, request, jsonify, abort, Response

from backend.model.user import User
from backend.view.response import ResponseStrings
from backend import db

blueprint = Blueprint('auth', __name__)


@blueprint.route('/auth/login', methods=('POST',))
def login():
    '''Authenticate user based on sent login and password.

    If password and login are correct generate and send token.

    Returns:
       dict: returns dict with status, token and user name if user is authenticated successfully,
           otherwise send dict with status 'failed' and message.

       Example:
        {
            'status': 'success',
            'token': 'TokenString',
            'name': 'admin'
        }
    '''
    data = request.get_json()
    user = User.query.filter_by(login=data.get('login')).first()
    invalid_credentials_response = jsonify({
        ResponseStrings.STATUS.value: ResponseStrings.FAILED.value,
        ResponseStrings.MESSAGE.value: 'Credentials are not valid'
    })

    if not user:
        return invalid_credentials_response, 400

    is_valid = User.check_password(data.get('password'), user.password)

    if not is_valid:
        return invalid_credentials_response, 400

    token = user.encode_auth_token().decode('utf8')
    return jsonify({
        ResponseStrings.STATUS.value: ResponseStrings.SUCCESS.value,
        ResponseStrings.TOKEN.value: token,
        ResponseStrings.NAME.value: user.login
    }), 200


@blueprint.route('/auth/register', methods=('POST',))
def register():
    '''Register user with login and password.

    Login has min length of 3 symbols and password has 6 symbols. Login must also be unique.

    Returns:
       dict: returns dict with status, token and user name if user is registered successfully,
           otherwise send dict with status 'failed'.

       Example:
        {
            'status': 'success',
            'token': 'TokenString',
            'name': 'admin'
        }
    '''
    data = request.get_json()
    user = User.query.filter_by(login=data.get('login')).first()
    if user:
        return jsonify({
            ResponseStrings.STATUS.value: ResponseStrings.FAILED.value,
            ResponseStrings.MESSAGE.value: 'Login is not unique'
        }), 400

    if len(data.get('login')) < 3 and len(data.get('password')) < 6:
        return jsonify({
            ResponseStrings.STATUS.value: ResponseStrings.FAILED.value,
            ResponseStrings.MESSAGE.value: "Credentials doesn't met requirements"
        }), 400

    user = User(
        login=data.get('login'),
        password=data.get('password')
    )
    db.session.add(user)
    db.session.commit()

    token = user.encode_auth_token().decode('utf8')
    return jsonify({
            ResponseStrings.STATUS.value: ResponseStrings.SUCCESS.value,
            ResponseStrings.TOKEN.value: token,
            ResponseStrings.NAME.value: user.login
        }), 201

@blueprint.route('/auth/logout', methods=('POST',))
def logout():
    '''Logout user.

    If sent token is valid, blacklist it (causing user logout).

    Returns:
       dict: returns dict with status.

       Example:
        {
            'status': 'success'
        }
    '''
    pass

@blueprint.route('/auth/user', methods=('GET',))
def get_user_info():
    '''Send information about user.

    If token is correct send user information.

    Returns:
        dict: returns fict with information about user.
    '''
    pass
