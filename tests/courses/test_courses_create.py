import pytest
from mathapp.curriculum.data_mapper.course.orm_course import ORMCourse
from mathapp.curriculum.data_mapper.lesson_sequence_item.orm_lesson_sequence_item import ORMLessonSequenceItem



def test_get_create_course_form(client, auth):
	auth.login()
	response = client.get('/create')
	assert response.status_code == 200

def test_get_create_course_form_not_authenticated_redirects(client):
	response = client.get('/create')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'



def test_post_create_form_valid(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	name = 'test_post_create_form_creates_course'
	display_name = 'display name'
	response = client.post('/create', data = {'name': name, 'display_name': display_name, 'csrf_token': csrf_token})
	assert 'http://localhost/' == response.headers.get('Location')
	course = sqlalchemy_session.query(ORMCourse).filter(ORMCourse.name == name).first()
	assert course is not None
	assert course.name == name

def test_create_missing_name(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/create', data = {'csrf_token': csrf_token})
	assert b'Course requires name' in response.data

def test_create_blank_name(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/create', data = {'name': ' ', 'csrf_token': csrf_token})
	assert b'Invalid name for course' in response.data

def test_create_duplicate_name(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/create', data = {'name': 'Test Get Course', 'csrf_token': csrf_token})
	assert b'Course name must be unique' in response.data

def test_create_not_authenticated(client, auth):
	response = client.post('/create', data = {'name': 'Test Get Course'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_create_no_csrf_token(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/create', data = {'name': 'Test Get Course'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_create_invalid_csrf_token(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/create', data = {'name': 'Test Get Course', 'csrf_token': 'invalid_token'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

