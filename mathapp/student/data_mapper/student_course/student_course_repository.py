from mathapp.student.data_mapper.student_course.orm_student_course import ORMStudentCourse
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError
from mathapp.libraries.general_library.errors.mathapp_error import MathAppError

class StudentCourseRepository:

	def __init__(self,
				 user_data,
				 unit_of_work,
				 session):
		self._user_data = user_data
		self._unit_of_work = unit_of_work
		self._session = session

	def get(self, student_course_id):
		student = self._get_student()
		orm_student_course = self._session.query(ORMStudentCourse) \
			.filter(ORMStudentCourse.id == student_course_id) \
			.filter(ORMStudentCourse.student_id == student['id']).first()
		if orm_student_course is None:
			raise NotFoundError(message = "StudentCourse not found")

		student_course = orm_student_course.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_student_course])

		return student_course


	def get_by_course_id(self, course_id):
		student = self._get_student()
		orm_student_course = self._session.query(ORMStudentCourse) \
			.filter(ORMStudentCourse.course_id == course_id) \
			.filter(ORMStudentCourse.student_id == student['id']).first()
		if orm_student_course is None:
			raise NotFoundError(message = "StudentCourse not found")

		student_course = orm_student_course.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_student_course])

		return student_course


	def _get_student(self):
		roles = self._user_data['roles']
		student = next(x for x in roles if x['type'] == 'student')
		if student is not None:
			return student
		else:
			raise MathAppError('StudentCourseRepository cannot find student')

