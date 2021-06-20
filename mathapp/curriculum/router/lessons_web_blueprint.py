from flask import (
	Blueprint, request
)
from mathapp.system.router.auth_web_blueprint import web_auth_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('lessons', __name__)

@bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>', methods=('GET', 'POST'))
@web_auth_required
def edit(course_id, lesson_id):
	if request.method == 'GET':
		return controller(request).get_edit_form(course_id=course_id, lesson_id=lesson_id)
	elif request.method == 'POST':
		return controller(request).post_edit_form(course_id=course_id, lesson_id=lesson_id)


def controller(request):
	return RootComposer(request).get_curriculum_controller_composer().compose_lesson_web_controller()
