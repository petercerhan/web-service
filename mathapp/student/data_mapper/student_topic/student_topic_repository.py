from mathapp.student.data_mapper.student_topic.orm_student_topic import ORMStudentTopic
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError
from mathapp.libraries.general_library.errors.mathapp_error import MathAppError


class StudentTopicRepository:

    def __init__(self,
                 user_data,
                 unit_of_work,
                 session):
        self._user_data = user_data
        self._unit_of_work = unit_of_work
        self._session = session

    def get(self, student_topic_id):
        student = self._get_student()
        orm_student_topic = self._session.query(ORMStudentTopic) \
            .filter(ORMStudentTopic.id == student_topic_id) \
            .first()
        if orm_student_topic is None:
            raise NotFoundError(message = f'StudentTopic id {student_topic_id} not found')
        self._unit_of_work.register_queried([orm_student_topic])

        student_topic = orm_student_topic.get_model(unit_of_work=self._unit_of_work)
        return student_topic


    def _get_student(self):
        roles = self._user_data['roles']
        student = next(x for x in roles if x['type'] == 'student')
        if student is not None:
            return student
        else:
            raise MathAppError('StudentCourseRepository cannot find student')

