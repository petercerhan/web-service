from flask import (
    Blueprint, request, g
)
from mathapp.system.router.api_auth_required import api_auth_required
from mathapp.main.root_composer import RootComposer

bp = Blueprint('student_topics.api', __name__)

@bp.route('/api/student_topics/<int:student_topic_id>/next-lesson-completable')
@api_auth_required
def get_next_lesson_completable(student_topic_id):
    return controller(request).get_next_lesson_completable(student_topic_id=student_topic_id)

@bp.route('/api/student_topics/<int:student_topic_id>/complete-lesson', methods=('POST',))
@api_auth_required
def complete_lesson(student_topic_id):
    return controller(request).complete_lesson(student_topic_id=student_topic_id)

@bp.route('/api/student_topics/<int:student_topic_id>/record-lesson-aborted', methods=('POST',))
@api_auth_required
def record_lesson_aborted(student_topic_id):
    return controller(request).record_lesson_aborted(student_topic_id=student_topic_id)


def controller(request):
    return RootComposer(request=request, user_data=g.user).get_student_controller_composer().compose_student_topic_api_controller()



