import os
import logging

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
# import psycopg2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

def create_app():
    app = Flask(__name__)
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    except KeyError:
        logger.error('You have to set database uri'
                     '(enviromental variable DB_URI) first.')
        exit()

    db.init_app(app)

    register_blueprints(app)
    register_error_handlers(app)

    from backend.model.tournament import Tournament
    from backend.model.participant import Participant, Paring

    init_db(app)
    app.debug = True

    return app

def register_blueprints(app):
    from backend.view import main
    from backend.view import participant
    from backend.view import tournament

    app.register_blueprint(main.blueprint)
    app.register_blueprint(participant.blueprint)
    app.register_blueprint(tournament.blueprint)

def register_error_handlers(app):
    from backend.view import error
    app.register_error_handler(404, error.page_not_found)
