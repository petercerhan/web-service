from mathapp.student.interactor.domain_to_data_transforms.student_course import student_course_to_data
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError

class StudentInteractor:

	def __init__(self,
				 student_course_repository,
				 unit_of_work):
		self._student_course_repository = student_course_repository
		self._unit_of_work = unit_of_work

	def initialize_student_course(self, student_id, course_id):
		##confirm no student course exists for this student, course
		student_course = self._find_student_course_for_course(course_id)
		if student_course is not None:
			return student_course_to_data(student_course)

		##Create student course record
		###Get Student
		###provide: CoursePushControl, Course(which provides topics), StudentCourseFactory, StudentTopicFactory
		return 'StudentInteractor initialize_student_course'

	def _find_student_course_for_course(self, course_id):
		try:
			student_course = self._student_course_repository.get_by_course_id(course_id=course_id)
			return student_course
		except NotFoundError as error:
			return None


