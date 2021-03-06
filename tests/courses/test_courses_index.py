import pytest
from mathapp.curriculum.data_mapper.course.orm_course import ORMCourse
from mathapp.curriculum.data_mapper.lesson_sequence_item.orm_lesson_sequence_item import ORMLessonSequenceItem
from flask import url_for


def test_get_courses_index(client, auth):
	auth.login()
	response = client.get(url_for('courses.index'))
	assert response.status_code == 200

def test_get_courses_index_not_authenticated_redirects(client):
	response = client.get(url_for('courses.index'))
	assert response.status_code == 302
	assert response.headers.get('Location') == 'http://localhost/auth/login'