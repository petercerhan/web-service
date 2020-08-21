import os

import pytest
from mathapp import create_app

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def app():
	app = create_app({'Testing': True})
	return app

@pytest.fixture
def client(app):
	return app.test_client()

class AuthActions(object):
	def __init__(self, client):
		self._client = client

	def login(self, username='peter3', password='abc123'):
		return self._client.post(
			'/auth/login',
			data={'username': username, 'password': password}
		)

	def logout(self):
		return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
	return AuthActions(client)

@pytest.fixture
def sqlalchemy_session():
	default_engine = create_engine('sqlite:///instance/test.sqlite')
	return scoped_session(sessionmaker(bind=default_engine))
