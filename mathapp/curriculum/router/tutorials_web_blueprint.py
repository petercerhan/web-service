from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('tutorials', __name__)

@bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>/create-tutorial', methods=('GET', 'POST'))
def create(course_id, lesson_id):
	if request.method == 'GET':
		return controller(request).get_create_form(course_id, lesson_id)
	elif request.method == 'POST':
		return controller(request).post_create_form(course_id, lesson_id)



def controller(request):
	return RootComposer(request).compose_tutorial_web_controller()
