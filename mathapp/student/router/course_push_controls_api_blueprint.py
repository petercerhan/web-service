from flask import (
    Blueprint, request, g
)
from mathapp.system.router.api_auth_required import api_auth_required
from mathapp.main.root_composer import RootComposer

bp = Blueprint('course_push_controls.api', __name__)

@bp.route('/api/courses/<int:course_id>/course_push_control')
@api_auth_required
def get_by_course_id(course_id):
    return controller(request).get_by_course_id(course_id=course_id)



def controller(request):
    return RootComposer(request).get_student_controller_composer().compose_course_push_control_api_controller()
