from mathapp.student.interactor.domain_to_data_transforms.student_course import student_course_to_data
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError

class StudentInteractor:

	def __init__(self,
				 student_repository,
				 student_course_repository,
				 course_push_control_repository,
				 course_repository,
				 student_course_factory,
				 student_topic_factory,
				 unit_of_work):
		self._student_course_repository = student_course_repository
		self._student_repository = student_repository
		self._course_push_control_repository = course_push_control_repository
		self._course_repository = course_repository
		self._student_course_factory = student_course_factory
		self._student_topic_factory = student_topic_factory
		self._unit_of_work = unit_of_work

	def initialize_student_course(self, student_id, course_id):
		existing_student_course = self._find_student_course_for_course(course_id)
		if existing_student_course is not None:
			return student_course_to_data(existing_student_course)

		student = self._student_repository.get(id=student_id)
		course_push_control = self._course_push_control_repository.get_by_course_id(course_id=course_id)
		course = self._course_repository.get(id=course_id)
		
		student_course = student.initialize_student_course(course=course,
										  				   course_push_control=course_push_control,
										  				   student_course_factory=self._student_course_factory,
										  				   student_topic_factory=self._student_topic_factory)

		self._unit_of_work.commit()

		return student_course_to_data(student_course)

	def _find_student_course_for_course(self, course_id):
		try:
			student_course = self._student_course_repository.get_by_course_id(course_id=course_id)
			return student_course
		except NotFoundError as error:
			return None


