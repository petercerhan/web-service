from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('tutorial_steps', __name__)

@bp.route('/courses/<int:course_id>/tutorials/<int:tutorial_id>/create-text-tutorial-step', methods=('POST', ))
@login_required
def create_text_tutorial_step(course_id, tutorial_id):
	return controller(request).post_create_text_step_form(course_id=course_id, tutorial_id=tutorial_id)

@bp.route('/courses/<int:course_id>/tutorials/<int:tutorial_id>/create-formula-tutorial-step', methods=('POST', ))
@login_required
def create_formula_tutorial_step(course_id, tutorial_id):
	return controller(request).post_create_formula_step_form(course_id=course_id, tutorial_id=tutorial_id)

@bp.route('/courses/<int:course_id>/tutorials/<int:tutorial_id>/text_tutorial_steps/<int:tutorial_step_id>', methods=('GET', 'POST'))
@login_required
def edit_text_tutorial_step(course_id, tutorial_id, tutorial_step_id):
	if request.method == 'GET':
		return controller(request).get_edit_text_tutorial_step_form(course_id=course_id, tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)
	elif request.method == 'POST':
		return controller(request).post_edit_text_tutorial_step_form(course_id=course_id, tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)

@bp.route('/courses/<int:course_id>/tutorials/<int:tutorial_id>/formula_tutorial_steps/<int:tutorial_step_id>', methods=('GET', 'POST'))
@login_required
def edit_formula_tutorial_step(course_id, tutorial_id, tutorial_step_id):
	if request.method == 'GET':
		return controller(request).get_edit_formula_tutorial_step_form(course_id=course_id, tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)
	elif request.method == 'POST':
		return controller(request).post_edit_formula_tutorial_step_form(course_id=course_id, tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)

@bp.route('/courses/<int:course_id>/tutorials/<int:tutorial_id>/tutorial_steps/<int:tutorial_step_id>/delete', methods=('POST', ))
@login_required
def delete(course_id, tutorial_id, tutorial_step_id):
	return controller(request).delete(course_id=course_id, tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)


def controller(request):
	return RootComposer(request).compose_tutorial_step_web_controller()
