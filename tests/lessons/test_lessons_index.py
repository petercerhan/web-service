import pytest
from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson


def test_get_lessons_index(client, auth):
	auth.login()
	response = client.get('/lessons/')
	assert response.status_code == 200

def test_get_lessons_index_not_authenticated(client):
	response = client.get('/lessons/')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'