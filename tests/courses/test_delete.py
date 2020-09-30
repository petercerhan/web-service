import pytest
from mathapp.curriculum.data_mapper.course.orm_course import ORMCourse
from mathapp.curriculum.data_mapper.lesson_sequence_item.orm_lesson_sequence_item import ORMLessonSequenceItem

def test_delete(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/14/delete', data = {'csrf_token': csrf_token})
	assert 'http://localhost/' == response.headers.get('Location')
	course = sqlalchemy_session.query(ORMCourse).filter(ORMCourse.id == 14).first()
	assert course is None

def test_delete_not_found(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/10000/delete', data = {'csrf_token': csrf_token})
	assert response.status_code == 404

def test_delete_not_authenticated(client):
	response = client.post('/14/delete')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_delete_no_csrf_token(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/14/delete')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'
	

def test_delete_lesson_sequence_item(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/15/lesson_sequence_items/4/delete', data = {'csrf_token': csrf_token})
	assert 'http://localhost/15' == response.headers.get('Location')
	lesson_sequence_item = sqlalchemy_session.query(ORMLessonSequenceItem).filter(ORMLessonSequenceItem.id == 4).first()
	assert lesson_sequence_item is None

def test_delete_lesson_sequence_item_not_authenticated(client):
	response = client.post('/15/lesson_sequence_items/4/delete')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_delete_lesson_sequence_item_no_csrf_token(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/15/lesson_sequence_items/4/delete')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'