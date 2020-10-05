from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('lesson_intros', __name__)

@bp.route('/lessons/<int:lesson_id>/lesson_sections/create_lesson_intro', methods=('GET', 'POST'))
@login_required
def create_lesson_intro(lesson_id):
	return controller(request).handle_create_request(lesson_id=lesson_id)

def controller(request):
	return RootComposer(request).compose_lesson_intro_web_controller()