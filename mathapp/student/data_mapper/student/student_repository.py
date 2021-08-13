from mathapp.student.data_mapper.student.orm_student import ORMStudent
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError
from mathapp.libraries.general_library.errors.mathapp_error import MathAppError

class StudentRepository:

    def __init__(self,
                 user_data,
                 unit_of_work,
                 session):
        self._user_data = user_data
        self._unit_of_work = unit_of_work
        self._session = session

    def get(self, id):
        student_id = self._get_student_id()
        if id != student_id:
            raise MathAppError(message="Access to this student not allowed")

        orm_student = self._session.query(ORMStudent).filter(ORMStudent.id == id).first()
        if orm_student is None:
            raise NotFoundError(message="Student not found")

        student = orm_student.get_model(unit_of_work=self._unit_of_work)
        self._unit_of_work.register_queried([orm_student])

        return student


    def _get_student_id(self):
        roles = self._user_data['roles']
        student = next(x for x in roles if x['type'] == 'student')
        if student is not None:
            return student['id']
        else:
            raise MathAppError('StudentCourseRepository cannot find student')

