from flask import (
    Blueprint, request, g
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('problem_set_generators', __name__)

@bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>/create-list-problem-set-generator', methods=('GET', 'POST'))
@login_required
def create_list_problem_set_generator(course_id, lesson_id):
    if request.method == 'GET':
        return controller(request).get_create_list_problem_set_generator_form(course_id=course_id, lesson_id=lesson_id)
    elif request.method == 'POST':
        return controller(request).post_create_list_problem_set_generator_form(course_id=course_id, lesson_id=lesson_id)


def controller(request):
    return RootComposer(request).compose_problem_set_generator_web_controller()


