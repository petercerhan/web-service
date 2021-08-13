from mathapp.student.data_mapper.course_push_control.course_push_control_repository import CoursePushControlRepository
from mathapp.student.data_mapper.student_course.student_course_repository import StudentCourseRepository
from mathapp.student.data_mapper.student.student_repository import StudentRepository

class StudentRepositoryComposer:

    def __init__(self,
                 user_data,
                 unit_of_work,
                 sqlalchemy_session):
        self._user_data = user_data
        self._unit_of_work = unit_of_work
        self._sqlalchemy_session = sqlalchemy_session

    def compose_course_push_control_repository(self):
        return CoursePushControlRepository(unit_of_work=self._unit_of_work,
                                           session=self._sqlalchemy_session)

    def compose_student_course_repository(self):
        return StudentCourseRepository(user_data=self._user_data,
                                       unit_of_work=self._unit_of_work,
                                       session=self._sqlalchemy_session)

    def compose_student_repository(self):
        return StudentRepository(user_data=self._user_data,
                                 unit_of_work=self._unit_of_work,
                                 session=self._sqlalchemy_session)
