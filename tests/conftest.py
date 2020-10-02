import os

import pytest
from mathapp import create_app

from mathapp.infrastructure_services.encryption_service import EncryptionService

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import sys

@pytest.fixture
def app():
	app = create_app({'Testing': True, 
						'SECRET_KEY': 'test', 
						'AUTH_SECRET_KEY': 'test_auth_secret_key', 
						'CSRF_HASH_KEY': 'test_csrf_hash_key'})
	return app

@pytest.fixture
def client(app):
	print("create app", file=sys.stderr)
	return app.test_client()

class AuthActions(object):
	def __init__(self, client):
		self._client = client

	def login(self, username='test_user', password='abc123'):
		response = self._client.post(
			'/auth/login',
			data={'username': username, 'password': password}
		)
		return response

	def login_return_csrf_token(self, username='test_user', password='abc123'):
		response = self._client.post(
			'/auth/login',
			data={'username': username, 'password': password}
		)
		cookie = next( (cookie for cookie in self._client.cookie_jar if cookie.name == 'auth_token'), None )
		auth_token = cookie.value

		encryption_service = EncryptionService('test_csrf_hash_key')
		csrf_token = encryption_service.generate_hash_for_csrf(auth_token)
		return csrf_token

	def logout(self):
		return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
	return AuthActions(client)

@pytest.fixture
def sqlalchemy_session():
	default_engine = create_engine('sqlite:///instance/test.sqlite')
	SessionFactory = scoped_session(sessionmaker(bind=default_engine))
	session = SessionFactory()
	return session
