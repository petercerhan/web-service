import pytest
from mathapp.curriculum.data_mapper.course.orm_course import ORMCourse
from mathapp.curriculum.data_mapper.lesson_sequence_item.orm_lesson_sequence_item import ORMLessonSequenceItem



def test_get_update_form(client, auth):
	auth.login()
	response = client.get('/1')
	assert response.status_code == 200

def test_get_update_form_not_authenticated(client):
	response = client.get('/1')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_get_update_form_not_found(client, auth):
	auth.login()
	response = client.get('/10000')
	assert response.status_code == 404



def test_update(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	display_name = 'test_update_course'
	response = client.post('/12', data = {'display_name': display_name, 'lesson_sequence_items': '[]', 'csrf_token': csrf_token})
	assert 'http://localhost/' == response.headers.get('Location')
	course = sqlalchemy_session.query(ORMCourse).filter(ORMCourse.id == 12).first()
	assert course is not None
	assert course.display_name == display_name

def test_update_invalid_display_name(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/13', data = {'display_name': '   ', 'lesson_sequence_items': '[]', 'csrf_token': csrf_token})
	assert b'Invalid display_name for course' in response.data
	course = sqlalchemy_session.query(ORMCourse).filter(ORMCourse.id == 13).first()
	assert course.name == 'Test Update Failed Course'

def test_update_not_found(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/10000', data = {'display_name': 'Test name', 'lesson_sequence_items': '[]', 'csrf_token': csrf_token})
	assert response.status_code == 404

def test_update_not_authenticated(client):
	response = client.post('/1', data = {'display_name': 'Test name', 'lesson_sequence_items': '[]'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_update_no_csrf_token(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/1', data = {'display_name': 'Test name', 'lesson_sequence_items': '[]'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'