import pytest
from mathapp.flask.db import Session
from mathapp.system.data_mapper.user.orm_user import ORMUser
from flask import g, session

def test_register_get_form(client):
    assert client.get('/auth/register').status_code == 200


def test_register(client, sqlalchemy_session):
    username = 'test_register_valid_credentials'
    response = client.post('/auth/register', data={'username': username, 'password': 'a'})
    assert 'http://localhost/auth/login' == response.headers.get('Location')
    user = sqlalchemy_session.query(ORMUser).filter(ORMUser.username == username).first()
    assert user is not None
    assert user.username == username


def test_register_duplicate(client):
    response = client.post('/auth/register', data={'username': 'test_register_duplicate', 'password': 'a'})
    response = client.post('/auth/register', data={'username': 'test_register_duplicate', 'password': 'a'})
    assert b'already registered' in response.data



def test_login_get_form(client):
    assert client.get('/auth/login').status_code == 200


def test_login(client, auth):
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['user_id'] == 3
        assert g.user['username'] == 'peter3'


def test_login_missing_user(client, auth):
    response = auth.login('test', 'test')
    assert b'Invalid Login' in response.data


def test_log_incorrect_password(client, auth):
    response = auth.login('peter3', 'wrongpassword')
    assert b'Invalid Login' in response.data