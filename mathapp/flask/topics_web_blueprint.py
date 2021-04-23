from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('topics', __name__)

@bp.route('/topics/')
@login_required
def index():
	return controller(request).get_index()

@bp.route('/courses/<int:course_id>/create-topic', methods=('GET', 'POST'))
@login_required
def create(course_id):
	if request.method == 'GET':
		return controller(request).get_create_form(course_id)
	elif request.method == 'POST':
		return controller(request).post_create_form(course_id)

@bp.route('/courses/<int:course_id>/topics/<int:topic_id>', methods=('GET', 'POST'))
@login_required
def edit(course_id, topic_id):
	if request.method == 'GET':
		return controller(request).get_edit_form(course_id=course_id, topic_id=topic_id)
	elif request.method == 'POST':
		return controller(request).post_edit_form(course_id, topic_id)

@bp.route('/courses/<int:course_id>/topics/<int:topic_id>/create-lesson', methods=('GET', 'POST'))
@login_required
def create_lesson(course_id, topic_id):
	return controller(request).get_create_lesson_form(course_id, topic_id)

def controller(request):
	return RootComposer(request).compose_topic_web_controller()
