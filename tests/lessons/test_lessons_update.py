import pytest
from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson


def test_get_update_form(client, auth):
	auth.login()
	response = client.get('/lessons/1')
	assert response.status_code == 200

def test_get_update_form_not_authenticated(client):
	response = client.get('/lessons/1')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'


def test_update(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	display_name = 'test_lessons_web.test_update'
	response = client.post('/lessons/1', data = {'display_name': display_name, 'lesson_sections': '[]', 'csrf_token': csrf_token})
	assert 'http://localhost/lessons/' == response.headers.get('Location')
	lesson = sqlalchemy_session.query(ORMLesson).filter(ORMLesson.display_name == display_name).first()
	assert lesson is not None
	assert lesson.display_name == display_name

def test_update_invalid_display_name(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/lessons/4', data = {'display_name': ' ', 'lesson_sections': '[]', 'csrf_token': csrf_token})
	assert b'Invalid display name for lesson' in response.data
	lesson = sqlalchemy_session.query(ORMLesson).filter(ORMLesson.id == 4).first()
	assert lesson.display_name == 'Test Update Failed Lesson'	

def test_update_not_found(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/lessons/10000', data = {'display_name': ' ', 'lesson_sections': '[]', 'csrf_token': csrf_token})
	assert response.status_code == 404

def test_update_not_authenticated(client):
	response = client.post('/lessons/1', data = {'display_name': 'test', 'lesson_sections': '[]', 'csrf_token': 'xxx'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_update_no_csrf_token(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/lessons/1', data = {'display_name': 'test', 'lesson_sections': '[]'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'