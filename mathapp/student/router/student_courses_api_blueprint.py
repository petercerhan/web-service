from flask import (
    Blueprint, request, g
)
from mathapp.system.router.api_auth_required import api_auth_required
from mathapp.main.root_composer import RootComposer

bp = Blueprint('student_courses.api', __name__)

@bp.route('/api/student_courses/<int:student_course_id>')
@api_auth_required
def get(student_course_id):
    return controller(request).get(student_course_id=student_course_id)


def controller(request):
    return RootComposer(request=request, user_data=g.user).get_student_controller_composer().compose_student_course_api_controller()

