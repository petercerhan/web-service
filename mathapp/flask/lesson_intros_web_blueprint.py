from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('lesson_intros', __name__)

@bp.route('/lessons/<int:lesson_id>/lesson_sections/create_lesson_intro', methods=('GET', 'POST'))
@login_required
def create(lesson_id):
	return controller(request).handle_create_request(lesson_id=lesson_id)

@bp.route('/lessons/<int:lesson_id>/lesson_intros/<int:lesson_section_id>', methods=('GET', 'POST'))
@login_required
def update(lesson_id, lesson_section_id):
	return controller(request).handle_update_request(lesson_id=lesson_id, lesson_section_id=lesson_section_id)

@bp.route('/lessons/<int:lesson_id>/lesson_intros/<int:lesson_section_id>/create_detail_section', methods=('POST',))
@login_required
def create_detail_section(lesson_id, lesson_section_id):
	return controller(request).handle_create_detail_section_request(lesson_id, lesson_section_id)

@bp.route('/lessons/<int:lesson_id>/lesson_intros/<int:lesson_section_id>/instruction_sections/<int:instruction_section_id>/delete', methods=('POST',))
@login_required
def delete_instruction_section(lesson_id, lesson_section_id, instruction_section_id):
	return controller(request).handle_delete_instruction_section_request(lesson_id, lesson_section_id, instruction_section_id)



def controller(request):
	return RootComposer(request).compose_lesson_intro_web_controller()


