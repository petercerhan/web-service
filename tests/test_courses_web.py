import pytest
from mathapp.flask.db import Session


def test_get_courses_index(client, auth):
	auth.login()
	response = client.get('/')
	assert response.status_code == 200

def test_get_courses_index_not_authenticated_redirects(client):
	response = client.get('/')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

