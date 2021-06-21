from flask import (
    Blueprint, request, g
)
from mathapp.system.router.web_auth_required import web_auth_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('exercises', __name__)


@bp.route('/topics/<int:topic_id>/create-formula-exercise', methods=('GET', 'POST'))
@web_auth_required
def create_formula_exercise(topic_id):
	if request.method == 'GET':
		return controller(request).get_create_formula_exercise_form(topic_id=topic_id)
	elif request.method == 'POST':
		return controller(request).post_create_formula_exercise_form(topic_id=topic_id)


@bp.route('/topics/<int:topic_id>/create-diagram-exercise', methods=('GET', 'POST'))
@web_auth_required
def create_diagram_exercise(topic_id):
	if request.method == 'GET':
		return controller(request).get_create_diagram_exercise_form(topic_id=topic_id)
	elif request.method == 'POST':
		user_id = g.user_id
		return controller(request).post_create_diagram_exercise_form(topic_id=topic_id, user_id=user_id)


@bp.route('/formula_exercises/<int:exercise_id>', methods=('GET', 'POST'))
@web_auth_required
def edit_formula_exercise(exercise_id):
	if request.method == 'GET':
		return controller(request).get_edit_formula_exercise_form(exercise_id=exercise_id)
	elif request.method == 'POST':
		return controller(request).post_edit_formula_exercise_form(exercise_id=exercise_id)


@bp.route('/diagram_exercises/<int:exercise_id>', methods=('GET', 'POST'))
@web_auth_required
def edit_diagram_exercise(exercise_id):
	if request.method == 'GET':
		return controller(request).get_edit_diagram_exercise_form(exercise_id=exercise_id)
	elif request.method == 'POST':
		user_id = g.user_id
		return controller(request).post_edit_diagram_exercise_form(exercise_id=exercise_id, user_id=user_id)


@bp.route('/exercises/<int:exercise_id>/delete', methods=('POST',))
@web_auth_required
def delete(exercise_id):
	return controller(request).delete(exercise_id=exercise_id)


def controller(request):
	return RootComposer(request).get_curriculum_controller_composer().compose_exercise_web_controller()

