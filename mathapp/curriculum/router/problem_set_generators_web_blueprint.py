from flask import (
    Blueprint, request, g
)
from mathapp.system.router.auth_web_blueprint import web_auth_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('problem_set_generators', __name__)

@bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>/create-list-problem-set-generator', methods=('GET', 'POST'))
@web_auth_required
def create_list_problem_set_generator(course_id, lesson_id):
    if request.method == 'GET':
        return controller(request).get_create_list_problem_set_generator_form(course_id=course_id, lesson_id=lesson_id)
    elif request.method == 'POST':
        return controller(request).post_create_list_problem_set_generator_form(course_id=course_id, lesson_id=lesson_id)

@bp.route('/courses/<int:course_id>/list_problem_set_generators/<int:problem_set_generator_id>', methods=('GET', 'POST'))
@web_auth_required
def edit_list_problem_set_generator(course_id, problem_set_generator_id):
    if request.method == 'GET':
        return controller(request).get_edit_list_problem_set_generator_form(course_id=course_id, problem_set_generator_id=problem_set_generator_id)
    if request.method == 'POST':
        return controller(request).post_edit_list_problem_set_generator_form(course_id=course_id, problem_set_generator_id=problem_set_generator_id)

@bp.route('/courses/<int:course_id>/problem_set_generators/<int:problem_set_generator_id>/add-exercises', methods=('GET', 'POST'))
@web_auth_required
def add_exercises(course_id, problem_set_generator_id):
    if request.method == 'GET':
        return controller(request).get_add_exercises_form(course_id=course_id, problem_set_generator_id=problem_set_generator_id)
    elif request.method == 'POST':
        return controller(request).post_add_exercises_form(course_id=course_id, problem_set_generator_id=problem_set_generator_id)

@bp.route('/courses/<int:course_id>/problem_set_generators/<int:problem_set_generator_id>/exercises/<int:exercise_id>/remove', methods=('POST', ))
@web_auth_required
def remove_exercise(course_id, problem_set_generator_id, exercise_id):
    return controller(request).remove_exercise_from_generator(course_id, problem_set_generator_id, exercise_id)

def controller(request):
    return RootComposer(request).compose_problem_set_generator_web_controller()


