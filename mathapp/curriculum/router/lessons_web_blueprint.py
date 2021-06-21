from flask import (
	Blueprint, request
)
from mathapp.system.router.web_auth_required import web_auth_required
from mathapp.main.root_composer import RootComposer

bp = Blueprint('lessons', __name__)

@bp.route('/lessons/<int:lesson_id>', methods=('GET', 'POST'))
@web_auth_required
def edit(lesson_id):
	if request.method == 'GET':
		return controller(request).get_edit_form(lesson_id=lesson_id)
	elif request.method == 'POST':
		return controller(request).post_edit_form(lesson_id=lesson_id)


def controller(request):
	return RootComposer(request).get_curriculum_controller_composer().compose_lesson_web_controller()
