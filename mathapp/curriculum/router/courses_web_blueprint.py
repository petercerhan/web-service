from flask import (
    Blueprint, request
)
from mathapp.system.router.auth_web_blueprint import web_auth_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('courses', __name__)

## Index

@bp.route('/courses/')
@web_auth_required
def index():
    return controller(request).handle_index_request()

## Create

@bp.route('/courses/create', methods=('GET', 'POST'))
@web_auth_required
def create():
    return controller(request).handle_create_request()

## Update

@bp.route('/courses/<int:id>', methods=('GET', 'POST'))
@web_auth_required
def update(id):
    return controller(request).handle_update_request(id)

## Delete

@bp.route('/courses/<int:id>/delete', methods=('POST',))
@web_auth_required
def delete(id):
    return controller(request).handle_delete_request(id)


## Create CourseTopic

@bp.route('/courses/<int:course_id>/create-course-topic', methods=('GET', 'POST'))
@web_auth_required
def create_course_topic(course_id):
	if request.method == 'GET':
		topic_id = request.args['topic_id']
		return controller(request).get_create_course_topic_form(course_id, topic_id)
	elif request.method == 'POST':
		return controller(request).post_create_course_topic_form(course_id)

## Delete CourseTopic

@bp.route('/courses/<int:course_id>/course-topics/<int:course_topic_id>/delete', methods=('POST',))
@web_auth_required
def delete_course_topic(course_id, course_topic_id):
    return controller(request).delete_course_topic(course_id=course_id, course_topic_id=course_topic_id)


## Util

def controller(request):
    return RootComposer(request).get_curriculum_controller_composer().compose_course_web_controller()
