from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('lessons', __name__)

## Index

@bp.route('/lessons/')
@login_required
def index():
	return controller(request).handle_index_request()

@bp.route('/lessons/create', methods=('GET', 'POST'))
@login_required
def create():
	return controller(request).handle_create_request()

@bp.route('/courses/<int:course_id>/lessons/create', methods=('GET', 'POST'))
@login_required
def createForCourse(course_id):
	return controller(request).handle_create_request()

@bp.route('/lessons/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
	return controller(request).handle_update_request(lesson_id=id)

@bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>', methods=('GET', 'POST'))
@login_required
def updateForCourse(course_id, lesson_id):
	return controller(request).handle_update_request(lesson_id=lesson_id, course_id=course_id)

@bp.route('/lessons/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
	return controller(request).handle_delete_request(id)

@bp.route('/lessons/<int:lesson_id>/lesson_sections/create')
@login_required
def create_lesson_section(lesson_id):
	return controller(request).handle_create_lesson_section_request(lesson_id)

@bp.route('/lessons/<int:lesson_id>/lesson_sections/<int:lesson_section_id>/delete', methods=('POST',))
@login_required
def delete_lesson_section(lesson_id, lesson_section_id):
	return controller(request).handle_delete_lesson_section_request(lesson_id=lesson_id, lesson_section_id=lesson_section_id)

## Util

def controller(request):
	return RootComposer(request).compose_lesson_web_controller()