import pytest


def test_empty_db(client):
    '''It should be empty database.'''
    response = client.get('/tournament')
    assert b'[]' in response.data