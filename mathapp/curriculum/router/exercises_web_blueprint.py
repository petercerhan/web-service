from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('exercises', __name__)


@bp.route('/courses/<int:course_id>/topics/<int:topic_id>/create-formula-exercise', methods=('GET', 'POST'))
@login_required
def create_formula_exercise(course_id, topic_id):
	if request.method == 'GET':
		return controller(request).get_create_formula_exercise_form(course_id=course_id, topic_id=topic_id)
	elif request.method == 'POST':
		return controller(request).post_create_formula_exercise_form(course_id=course_id, topic_id=topic_id)

@bp.route('/courses/<int:course_id>/topics/<int:topic_id>/create-diagram-exercise', methods=('GET', 'POST'))
@login_required
def create_diagram_exercise(course_id, topic_id):
	if request.method == 'GET':
		return controller(request).get_create_diagram_exercise_form(course_id=course_id, topic_id=topic_id)
	elif request.method == 'POST':
		# return controller(request).post_create_formula_exercise_form(course_id=course_id, topic_id=topic_id)
		return 'test'


def controller(request):
	return RootComposer(request).compose_exercise_web_controller()

