from mathapp.student.interactor.domain_to_data_transforms.course_push_control import course_push_control_to_data

class CoursePushControlInteractor:

	def __init__(self,
				 course_push_control_repository,
				 unit_of_work):
		self._course_push_control_repository = course_push_control_repository
		self._unit_of_work = unit_of_work

	def get_by_course_id(self, course_id):
		course_push_control = self._course_push_control_repository.get_by_course_id(course_id=course_id)
		return course_push_control_to_data(course_push_control)

		