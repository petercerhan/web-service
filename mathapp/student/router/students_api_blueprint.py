from flask import (
    Blueprint, request, g
)
from mathapp.system.router.api_auth_required import api_auth_required
from mathapp.main.root_composer import RootComposer

bp = Blueprint('students.api', __name__)

@bp.route('/api/students/<int:student_id>/initialize-student-course', methods=('POST',))
@api_auth_required
def initialize_student_course(student_id):
    return controller(request).initialize_student_course(student_id=student_id)


def controller(request):
    return RootComposer(request=request, user_data=g.user).get_student_controller_composer().compose_student_api_controller()
