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

def test_invalid_cred_registration(client):
    '''It should not register user. Data is malformed.'''
    credentials = {
        'login': ['user', '123'],
        'password': 0
    }

    with pytest.raises(Exception) as e:
        response = client.post('/auth/register',
                            data=json.dumps(credentials),
                            content_type='application/json')

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

def test_valid_userinfo(client):
    '''It should return user info.'''
    header = {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjQ1NzgwOTcsImlhdCI6MTU2NDQ5MTY5Nywic3ViIjoxfQ.B8j9JLENTH4YZtnODq316M_97py3RGDaNMpNcQFhx0E'
    }
    response = client.get('/auth/user',
                           headers=header)

    assert bytes(ResponseStrings.SUCCESS.value, encoding='utf-8') in response.data

def test_invalid_userinfo(client):
    '''It should not return user info.'''
    header = {
        'token': ''
    }
    response = client.get('/auth/user',
                           headers=header)

    assert bytes(ResponseStrings.FAILED.value, encoding='utf-8') in response.data

def test_valid_logout(client):
    '''It should logout user.'''
    header = {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjQ1NzgwOTcsImlhdCI6MTU2NDQ5MTY5Nywic3ViIjoxfQ.B8j9JLENTH4YZtnODq316M_97py3RGDaNMpNcQFhx0E'
    }
    response = client.post('/auth/logout',
                           data=json.dumps(dict()),
                           content_type='application/json',
                           headers=header)

    assert bytes(ResponseStrings.SUCCESS.value, encoding='utf-8') in response.data

def test_invalid_logout(client):
    '''It should not logout user.'''
    header = {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjQ0MzU3NzIsImlhdCI6MTU2NDM0OTM3Miwic3ViIjoyfQ.0qP0BdIdMAptcCQHaVKNbY_DYAQEKlT0NGb4xB'
    }
    response = client.post('/auth/logout',
                           data=json.dumps(dict()),
                           content_type='application/json',
                           headers=header)

    assert bytes(ResponseStrings.FAILED.value, encoding='utf-8') in response.data