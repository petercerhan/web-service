import pytest
from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson


def test_delete(client, auth, sqlalchemy_session):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/lessons/5/delete', data={'csrf_token': csrf_token})
	assert 'http://localhost/lessons/' == response.headers.get('Location')
	lesson = sqlalchemy_session.query(ORMLesson).filter(ORMLesson.id == 5).first()
	assert lesson is None

def test_delete_not_found(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('lessons/10000/delete', data = {'csrf_token': csrf_token})
	assert response.status_code == 404

def test_delete_not_authenticated(client):
	response = client.post('/lessons/5/delete', data={'csrf_token': 'xxx'})
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'

def test_delete_no_csrf_token(client, auth):
	csrf_token = auth.login_return_csrf_token()
	response = client.post('/lessons/5/delete')
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'