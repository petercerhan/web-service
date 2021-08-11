from mathapp.student.main.student_interactor_composer import StudentInteractorComposer
from mathapp.student.main.student_presenter_composer import StudentPresenterComposer

from mathapp.student.controller.course_push_control_controller import CoursePushControlController

class StudentControllerComposer:

	def __init__(self,
				 request,
				 sqlalchemy_session,
				 unit_of_work):
		self._request = request
		self._student_interactor_composer = StudentInteractorComposer(unit_of_work=unit_of_work,
																	  sqlalchemy_session=sqlalchemy_session)
		self._student_presenter_composer = StudentPresenterComposer()

	def compose_course_push_control_api_controller(self):
		course_push_control_interactor = self._student_interactor_composer.compose_course_push_control_interactor()
		course_push_control_api_presenter = self._student_presenter_composer.compose_course_push_control_api_presenter()
		return CoursePushControlController(request=self._request,
										   course_push_control_interactor=course_push_control_interactor,
										   course_push_control_api_presenter=course_push_control_api_presenter)

