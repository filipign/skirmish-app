import os
import tempfile

import pytest

from backend import create_app
from backend import init_db
from backend.model.user import User

# TODO: tests should use abstract database for unit testing
def load_data(db, app):
    with app.app_context():
        user = User(
            login='user',
            password='testpass'
        )
        db.session.add(user)
        db.session.commit()

@pytest.fixture
def app():
    '''Create and configure a new app instance for each test.'''
    test_db_uri = 'postgresql://test_skirmish:testskirmish@localhost/test_skirmish'
    app = create_app(db_uri=test_db_uri)

    db = init_db(app)

    load_data(db, app)

    yield app


@pytest.fixture
def client(app):
    '''A test client for the app.'''
    return app.test_client()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    return AuthActions(client)