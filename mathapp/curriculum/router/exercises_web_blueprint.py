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
		return 'blueprint placeholder'

def controller(request):
	return RootComposer(request).compose_exercise_web_controller()

