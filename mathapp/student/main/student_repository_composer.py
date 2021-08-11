from mathapp.student.data_mapper.course_push_control.course_push_control_repository import CoursePushControlRepository

class StudentRepositoryComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._sqlalchemy_session = sqlalchemy_session

    def compose_course_push_control_repository(self):
        return CoursePushControlRepository(unit_of_work=self._unit_of_work,
                                           session=self._sqlalchemy_session)
