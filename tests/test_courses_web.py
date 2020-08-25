import pytest
from mathapp.curriculum.data_mapper.course.orm_course import ORMCourse


## Index

def test_get_courses_index(client, auth):
	auth.login()
	response = client.get('/')
	assert response.status_code == 200

def test_get_courses_index_not_authenticated_redirects(client):
	response = client.get('/')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'


## Create

def test_get_create_course_form(client, auth):
	auth.login()
	response = client.get('/create')
	assert response.status_code == 200

def test_get_create_course_form_not_authenticated_redirects(client):
	response = client.get('/create')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_post_create_form_valid(client, auth, sqlalchemy_session):
	auth.login()

	name = 'test_post_create_form_creates_course'

	response = client.post('/create', data = {'name': name})
	assert 'http://localhost/' == response.headers.get('Location')
	course = sqlalchemy_session.query(ORMCourse).filter(ORMCourse.name == name).first()
	assert course is not None
	assert course.name == name

def test_create_missing_name(client, auth, sqlalchemy_session):
	auth.login()
	response = client.post('/create', data = {})
	assert b'Course requires name' in response.data

def test_create_blank_name(client, auth):
	auth.login()
	response = client.post('/create', data = {'name': ' '})
	assert b'Invalid name for course' in response.data

def test_create_duplicate_name(client, auth):
	auth.login()
	response = client.post('/create', data = {'name': 'Test Get Course'})
	assert b'Course name must be unique' in response.data


## Update

def test_get_update_form(client, auth):
	auth.login()
	response = client.get('/1/update')
	assert response.status_code == 200

def test_get_update_form_not_authenticated(client):
	response = client.get('/1/update')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_get_update_form_not_found(client, auth):
	auth.login()
	response = client.get('/10000/update')
	assert response.status_code == 404

def test_update(client, auth, sqlalchemy_session):
	auth.login()
	name = 'test_update_course'
	response = client.post('/1/update', data = {'name': name, 'lesson_sequence_items': '[]'})
	assert 'http://localhost/' == response.headers.get('Location')
	course = sqlalchemy_session.query(ORMCourse).filter(ORMCourse.name == name).first()
	assert course is not None
	assert course.name == name

def test_update_invalid_name(client, auth, sqlalchemy_session):
	auth.login()
	response = client.post('/13/update', data = {'name': '   ', 'lesson_sequence_items': '[]'})
	assert b'Invalid name for course' in response.data
	course = sqlalchemy_session.query(ORMCourse).filter(ORMCourse.id == 13).first()
	assert course.name == 'Test Update Failed Course'

def test_update_not_authenticated(client):
	response = client.post('/1/update', data = {'name': 'Test name', 'lesson_sequence_items': '[]'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_update_not_found(client, auth):
	auth.login()
	response = client.post('/10000/update', data = {'name': 'Test name', 'lesson_sequence_items': '[]'})
	assert response.status_code == 404


## Delete

def test_delete(client, auth, sqlalchemy_session):
	auth.login()
	response = client.post('/14/delete')
	assert 'http://localhost/' == response.headers.get('Location')
	course = sqlalchemy_session.query(ORMCourse).filter(ORMCourse.id == 14).first()
	assert course is None

def test_delete_not_authenticated(client):
	response = client.post('/14/delete')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_delete_not_found(client, auth):
	auth.login()
	response = client.post('/10000/delete')
	assert response.status_code == 404











