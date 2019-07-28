import os
import logging

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy()
secret_key = ''
db_uri = ''

try:
    secret_key = os.environ['SECRET_KEY']
    db_uri = os.environ['DB_URI']
except KeyError:
    logger.error('You have to set env variables (SECRET_KEY, DB_URI) first')
    exit()


def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        return db


def create_app(db_uri=db_uri):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.init_app(app)

    register_blueprints(app)
    register_error_handlers(app)

    from backend.model.tournament import Tournament
    from backend.model.participant import Participant, Paring
    from backend.model.user import User
    from backend.model.blacklist import TokenBlacklist

    # Used for db init:
    init_db(app)
    app.debug = True

    CORS(app)

    return app


def register_blueprints(app):
    from backend.view import main
    from backend.view import participant
    from backend.view import tournament
    from backend.view import auth

    app.register_blueprint(main.blueprint)
    app.register_blueprint(participant.blueprint)
    app.register_blueprint(tournament.blueprint)
    app.register_blueprint(auth.blueprint)


def register_error_handlers(app):
    from backend.view import error
    app.register_error_handler(404, error.page_not_found)
