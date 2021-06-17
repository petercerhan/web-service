from flask import (
    Blueprint, request, g
)
from mathapp.system.router.auth_web_blueprint import web_auth_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('exercises', __name__)


@bp.route('/courses/<int:course_id>/topics/<int:topic_id>/create-formula-exercise', methods=('GET', 'POST'))
@web_auth_required
def create_formula_exercise(course_id, topic_id):
	if request.method == 'GET':
		return controller(request).get_create_formula_exercise_form(course_id=course_id, topic_id=topic_id)
	elif request.method == 'POST':
		return controller(request).post_create_formula_exercise_form(course_id=course_id, topic_id=topic_id)

@bp.route('/courses/<int:course_id>/topics/<int:topic_id>/create-diagram-exercise', methods=('GET', 'POST'))
@web_auth_required
def create_diagram_exercise(course_id, topic_id):
	if request.method == 'GET':
		return controller(request).get_create_diagram_exercise_form(course_id=course_id, topic_id=topic_id)
	elif request.method == 'POST':
		user_id = g.user_id
		return controller(request).post_create_diagram_exercise_form(course_id=course_id, topic_id=topic_id, user_id=user_id)

@bp.route('/courses/<int:course_id>/formula_exercises/<int:exercise_id>', methods=('GET', 'POST'))
@web_auth_required
def edit_formula_exercise(course_id, exercise_id):
	if request.method == 'GET':
		return controller(request).get_edit_formula_exercise_form(course_id=course_id, exercise_id=exercise_id)
	elif request.method == 'POST':
		return controller(request).post_edit_formula_exercise_form(course_id=course_id, exercise_id=exercise_id)

@bp.route('/courses/<int:course_id>/diagram_exercises/<int:exercise_id>', methods=('GET', 'POST'))
@web_auth_required
def edit_diagram_exercise(course_id, exercise_id):
	if request.method == 'GET':
		return controller(request).get_edit_diagram_exercise_form(course_id=course_id, exercise_id=exercise_id)
	elif request.method == 'POST':
		user_id = g.user_id
		return controller(request).post_edit_diagram_exercise_form(course_id=course_id, exercise_id=exercise_id, user_id=user_id)

@bp.route('/courses/<int:course_id>/exercises/<int:exercise_id>/delete', methods=('POST',))
@web_auth_required
def delete(course_id, exercise_id):
	return controller(request).delete(course_id=course_id, exercise_id=exercise_id)


def controller(request):
	return RootComposer(request).compose_exercise_web_controller()

