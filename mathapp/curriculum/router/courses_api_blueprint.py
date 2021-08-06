from flask import (
    Blueprint, request
)
from mathapp.system.router.api_auth_required import api_auth_required
from mathapp.main.root_composer import RootComposer

bp = Blueprint('courses.api', __name__)


@bp.route('/api/courses/')
@api_auth_required
def list():
    return controller(request).list()


def controller(request):
    return RootComposer(request).get_curriculum_controller_composer().compose_course_api_controller()


