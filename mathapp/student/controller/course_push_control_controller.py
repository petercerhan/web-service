from mathapp.libraries.general_library.errors.mathapp_error import MathAppError

class CoursePushControlController:

	def __init__(self,
				 request,
				 course_push_control_interactor,
				 course_push_control_api_presenter):
		self._request = request
		self._course_push_control_interactor = course_push_control_interactor
		self._course_push_control_api_presenter = course_push_control_api_presenter

	def get_by_course_id(self, course_id):
		try:
			course_push_control = self._course_push_control_interactor.get_by_course_id(course_id=course_id)
			return self._course_push_control_api_presenter.single(course_push_control)
		except MathAppError as error:
			return self._course_push_control_api_presenter.error()

