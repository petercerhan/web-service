from flask import (
    Blueprint, request
)
from mathapp.system.router.web_auth_required import web_auth_required
from mathapp.main.root_composer import RootComposer

bp = Blueprint('tutorials', __name__)

@bp.route('/lessons/<int:lesson_id>/create-tutorial', methods=('GET', 'POST'))
@web_auth_required
def create(lesson_id):
	if request.method == 'GET':
		return controller(request).get_create_form(lesson_id)
	elif request.method == 'POST':
		return controller(request).post_create_form(lesson_id)


@bp.route('/tutorials/<int:tutorial_id>', methods=('GET', 'POST'))
@web_auth_required
def edit(tutorial_id):
	if request.method == 'GET':
		return controller(request).get_edit_form(tutorial_id=tutorial_id)
	elif request.method == 'POST':
		return controller(request).post_edit_form(tutorial_id=tutorial_id)


@bp.route('/tutorials/<int:tutorial_id>/delete', methods=('POST', ))
@web_auth_required
def delete(tutorial_id):
	return controller(request).delete(tutorial_id=tutorial_id)


def controller(request):
	return RootComposer(request).get_curriculum_controller_composer().compose_tutorial_web_controller()
