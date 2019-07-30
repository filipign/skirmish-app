'''Test cases for tournament view'''
import json

import pytest

from backend.view.response import ResponseStrings


def test_valid_tournament_registration(client):
    '''It should create tourament user.'''
    header = {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjQ1NzgwOTcsImlhdCI6MTU2NDQ5MTY5Nywic3ViIjoxfQ.B8j9JLENTH4YZtnODq316M_97py3RGDaNMpNcQFhx0E'
    }
    response = client.post('/tournament',
                           data=json.dumps(dict(name='test')),
                           content_type='application/json',
                           headers=header)

    assert bytes(ResponseStrings.SUCCESS.value, encoding='utf-8') in response.data

def test_invalid_tournament_registration(client):
    '''It should not create tourament with wrong token.'''
    header = {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjQ1NzgwOTcsImlhdCI6MTU2NDQ5MTY5Nywic3ViIjoxfQ.B8j9JLENTH4YZtnODq316M_97py3RGDaNMpNcQFhx'
    }
    response = client.post('/tournament',
                           data=json.dumps(dict(name='test')),
                           content_type='application/json',
                           headers=header)

    assert bytes(ResponseStrings.FAILED.value, encoding='utf-8') in response.data

def test_invalid_name_tournament(client):
    '''It should not create tourament with malformed json data.'''
    header = {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjQ1NzgwOTcsImlhdCI6MTU2NDQ5MTY5Nywic3ViIjoxfQ.B8j9JLENTH4YZtnODq316M_97py3RGDaNMpNcQFhx0E'
    }
    response = client.post('/tournament',
                           data=json.dumps(dict(name=['test', ''])),
                           content_type='application/json',
                           headers=header)

    assert bytes(ResponseStrings.FAILED.value, encoding='utf-8') in response.data