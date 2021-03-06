from flask import (
    Blueprint, request, g
)
from mathapp.system.router.web_auth_required import web_auth_required
from mathapp.main.root_composer import RootComposer

bp = Blueprint('tutorial_steps', __name__)


@bp.route('/tutorials/<int:tutorial_id>/create-text-tutorial-step', methods=('POST', ))
@web_auth_required
def create_text_tutorial_step(tutorial_id):
	return controller(request).post_create_text_step_form(tutorial_id=tutorial_id)


@bp.route('/tutorials/<int:tutorial_id>/create-formula-tutorial-step', methods=('POST', ))
@web_auth_required
def create_formula_tutorial_step(tutorial_id):
	return controller(request).post_create_formula_step_form(tutorial_id=tutorial_id)


@bp.route('/tutorials/<int:tutorial_id>/create-image-tutorial-step', methods=('POST', ))
@web_auth_required
def create_image_tutorial_step(tutorial_id):
	return controller(request).post_create_image_step_form(tutorial_id=tutorial_id, user_id=g.user_id)


@bp.route('/tutorials/<int:tutorial_id>/text_tutorial_steps/<int:tutorial_step_id>', methods=('GET', 'POST'))
@web_auth_required
def edit_text_tutorial_step(tutorial_id, tutorial_step_id):
	if request.method == 'GET':
		return controller(request).get_edit_text_tutorial_step_form(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)
	elif request.method == 'POST':
		return controller(request).post_edit_text_tutorial_step_form(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)


@bp.route('/tutorials/<int:tutorial_id>/formula_tutorial_steps/<int:tutorial_step_id>', methods=('GET', 'POST'))
@web_auth_required
def edit_formula_tutorial_step(tutorial_id, tutorial_step_id):
	if request.method == 'GET':
		return controller(request).get_edit_formula_tutorial_step_form(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)
	elif request.method == 'POST':
		return controller(request).post_edit_formula_tutorial_step_form(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)


@bp.route('/tutorials/<int:tutorial_id>/image_tutorial_steps/<int:tutorial_step_id>', methods=('GET', 'POST'))
@web_auth_required
def edit_image_tutorial_step(tutorial_id, tutorial_step_id):
	if request.method == 'GET':
		return controller(request).get_edit_image_tutorial_step_form(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)
	elif request.method == 'POST':
		user_id = g.user_id
		return controller(request).post_edit_image_tutorial_step_form(user_id=user_id, tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)


@bp.route('/tutorials/<int:tutorial_id>/image_tutorial_steps/<int:tutorial_step_id>/download-source-code', methods=('GET', ))
@web_auth_required
def download_image_tutorial_step_source_code(tutorial_id, tutorial_step_id):
	return controller(request).download_image_tutorial_step_source_code(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)


@bp.route('/tutorials/<int:tutorial_id>/tutorial_steps/<int:tutorial_step_id>/delete', methods=('POST', ))
@web_auth_required
def delete(tutorial_id, tutorial_step_id):
	return controller(request).delete(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)


def controller(request):
	return RootComposer(request).get_curriculum_controller_composer().compose_tutorial_step_web_controller()




