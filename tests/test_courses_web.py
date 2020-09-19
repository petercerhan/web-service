import pytest
from mathapp.curriculum.data_mapper.course.orm_course import ORMCourse
from mathapp.curriculum.data_mapper.lesson_sequence_item.orm_lesson_sequence_item import ORMLessonSequenceItem


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


## Update

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


## Delete

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
	

## Delete Lesson Sequence item

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
	









