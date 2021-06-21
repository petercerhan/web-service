from flask import (
    Blueprint, request
)
from mathapp.system.router.web_auth_required import web_auth_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('topics', __name__)

@bp.route('/topics/')
@web_auth_required
def index():
	return controller(request).get_index()


@bp.route('/courses/<int:course_id>/create-topic', methods=('GET', 'POST'))
@web_auth_required
def create(course_id):
	if request.method == 'GET':
		return controller(request).get_create_form(course_id)
	elif request.method == 'POST':
		return controller(request).post_create_form(course_id)


@bp.route('/topics/<int:topic_id>', methods=('GET', 'POST'))
@web_auth_required
def edit(topic_id):
	if request.method == 'GET':
		return controller(request).get_edit_form(topic_id)
	elif request.method == 'POST':
		return controller(request).post_edit_form(topic_id)


@bp.route('/topics/<int:topic_id>/delete', methods=('POST',))
@web_auth_required
def delete(topic_id):
	return controller(request).delete(topic_id=topic_id)


@bp.route('/courses/<int:course_id>/topics/<int:topic_id>/create-lesson', methods=('GET', 'POST'))
@web_auth_required
def create_lesson(course_id, topic_id):
	if request.method == 'GET':
		return controller(request).get_create_lesson_form(course_id, topic_id)
	elif request.method == 'POST':
		return controller(request).post_create_lesson_form(course_id, topic_id)


@bp.route('/courses/<int:course_id>/topics/<int:topic_id>/lessons/<int:lesson_id>/delete', methods=('POST',))
@web_auth_required
def delete_lesson(course_id, topic_id, lesson_id):
	return controller(request).delete_lesson(course_id=course_id, topic_id=topic_id, lesson_id=lesson_id)


@bp.route('/courses/<int:course_id>/topics/<int:topic_id>/exercises', methods=('GET',))
@web_auth_required
def edit_exercises(course_id, topic_id):
	return controller(request).get_edit_exercises_form(course_id=course_id, topic_id=topic_id)



def controller(request):
	return RootComposer(request).get_curriculum_controller_composer().compose_topic_web_controller()















