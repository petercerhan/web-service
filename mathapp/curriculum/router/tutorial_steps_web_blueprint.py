from flask import (
    Blueprint, request
)
from mathapp.flask.auth_web_blueprint import login_required
from mathapp.flask.root_composer import RootComposer

bp = Blueprint('tutorial_steps', __name__)

@bp.route('/courses/<int:course_id>/tutorials/<int:tutorial_id>/create-text-tutorial-step', methods=('POST', ))
@login_required
def create_text_tutorial_step(course_id, tutorial_id):
	return controller(request).post_create_text_step_form(course_id=course_id, tutorial_id=tutorial_id)



def controller(request):
	return RootComposer(request).compose_tutorial_step_web_controller()
