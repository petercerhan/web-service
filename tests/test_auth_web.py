import pytest
from mathapp.system.data_mapper.user.orm_user import ORMUser
from flask import g, session, url_for

## Register

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

def test_register_no_username(client):
    response = client.post('/auth/register', data={'password': 'a'})
    assert b'User requires username' in response.data

def test_register_blank_username(client, sqlalchemy_session):
    response = client.post('/auth/register', data={'username': '   ', 'password': 'a'})
    assert b'Invalid username' in response.data

def test_register_no_password(client, sqlalchemy_session):
    response = client.post('/auth/register', data={'username': 'test_register_no_password'})
    assert b'User requires password' in response.data
    user = sqlalchemy_session.query(ORMUser).filter(ORMUser.username == 'test_register_no_password').first()
    assert user is None


## Login

def test_login_get_form(client):
    assert client.get('/auth/login').status_code == 200

def test_login(client, auth):
    response = auth.login()
    assert response.headers['Location'] == f'http://localhost{url_for("courses.index")}'

    with client:
        client.get(url_for("courses.index"))
        assert g.user_id == 1
        assert g.user_name == 'test_user'

def test_login_missing_user(client, auth):
    response = auth.login('test', 'test')
    assert b'Invalid Login' in response.data

def test_login_incorrect_password(client, auth):
    response = auth.login('test_user', 'wrongpassword')
    assert b'Invalid Login' in response.data




