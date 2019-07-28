'''Test cases for user login/logout'''
import json

import pytest
from backend.view.response import ResponseStrings

def test_valid_registration(client):
    '''It should register user.'''
    credentials = {
        'login': 'user2',
        'password': 'testpass'
    }
    response = client.post('/auth/register',
                           data=json.dumps(credentials),
                           content_type='application/json')

    assert bytes(ResponseStrings.SUCCESS.value, encoding='utf-8') in response.data
    assert bytes(ResponseStrings.TOKEN.value, encoding='utf-8') in response.data

def test_invalid_registration(client):
    '''It should not register user. User with that login already exist.'''
    credentials = {
        'login': 'user',
        'password': 'testpass'
    }
    response = client.post('/auth/register',
                           data=json.dumps(credentials),
                           content_type='application/json')

    assert bytes(ResponseStrings.FAILED.value, encoding='utf-8') in response.data

def test_valid_login(client):
    '''It should authenticate user.'''
    credentials = {
        'login': 'user',
        'password': 'testpass'
    }
    response = client.post('/auth/login',
                           data=json.dumps(credentials),
                           content_type='application/json')

    assert bytes(ResponseStrings.SUCCESS.value, encoding='utf-8') in response.data

def test_invalid_login(client):
    '''It should not authenticate user.'''
    credentials = {
        'login': 'user',
        'password': 'faketestpass'
    }
    response = client.post('/auth/login',
                           data=json.dumps(credentials),
                           content_type='application/json')

    assert bytes(ResponseStrings.FAILED.value, encoding='utf-8') in response.data

def test_valid_logout(client):
    '''It should logout user.'''
    header = {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjQ0MzU3NzIsImlhdCI6MTU2NDM0OTM3Miwic3ViIjoyfQ.0qP0BdIdMAptcCQHaVKNbY_DYAQEKlT0NGb4xB-wEeo'
    }
    response = client.post('/auth/logout',
                           data=json.dumps(dict()),
                           content_type='application/json',
                           headers=header)

    assert bytes(ResponseStrings.SUCCESS.value, encoding='utf-8') in response.data

def test_invalid_logout(client):
    '''It should not logout user.'''
    header = {
        'token': 'dIdMAptcCQHaVKNbY_DYAQEKlT0NGb4xB-wEeo'
    }
    response = client.post('/auth/logout',
                           data=json.dumps(dict()),
                           content_type='application/json',
                           headers=header)

    assert bytes(ResponseStrings.FAILED.value, encoding='utf-8') in response.data
