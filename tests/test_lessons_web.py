import pytest
from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson


## Index

def test_get_lessons_index(client, auth):
	auth.login()
	response = client.get('/lessons/')
	assert response.status_code == 200

def test_get_lessons_index_not_authenticated(client):
	response = client.get('/lessons/')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'


##Create

def test_get_create_lesson_form(client, auth):
	auth.login()
	response = client.get('/lessons/create')
	assert response.status_code == 200

def test_get_create_lesson_form_not_authenticated(client):
	response = client.get('/lessons/create')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'


def test_post_create_form_valid(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	name = 'test_lessons.test_post_create_form_valid'
	response = client.post('/lessons/create', data={'name': name, 'display_name': name, 'csrf_token': csrf_token})
	assert 'http://localhost/lessons/' == response.headers.get('Location')
	lesson = sqlalchemy_session.query(ORMLesson).filter(ORMLesson.name == name).first()
	assert lesson is not None
	assert lesson.name == name

def test_create_missing_name(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/lessons/create', data = {'csrf_token': csrf_token})
	assert b'Lesson requires name' in response.data

def test_create_blank_name(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/lessons/create', data = {'name': ' ', 'csrf_token': csrf_token})
	assert b'Invalid name for lesson' in response.data



def test_create_not_authenticated(client):
	response = client.post('/lessons/create', data={'name': 'test'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_create_no_csrf_token(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/lessons/create', data = {'name': 'Test Get Course'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'









