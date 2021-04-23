from flask import (
	Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('lessons', __name__)

@bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>', methods=('GET', 'POST'))
@login_required
def edit(course_id, lesson_id):
	return controller(request).get_edit_form(course_id=course_id, lesson_id=lesson_id)


def controller(request):
	return RootComposer(request).compose_lesson_web_controller()
