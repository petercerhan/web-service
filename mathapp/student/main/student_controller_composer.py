from mathapp.student.main.student_interactor_composer import StudentInteractorComposer
from mathapp.student.main.student_presenter_composer import StudentPresenterComposer

from mathapp.student.controller.course_push_control_controller import CoursePushControlController
from mathapp.student.controller.student_api_controller import StudentApiController
from mathapp.student.controller.student_course_api_controller import StudentCourseApiController

from mathapp.libraries.controller_library.api_error_handling_controller_decorator import ApiErrorHandlingControllerDecorator

class StudentControllerComposer:

	def __init__(self,
				 request,
				 user_data,
				 sqlalchemy_session,
				 unit_of_work):
		self._request = request
		self._student_interactor_composer = StudentInteractorComposer(user_data=user_data,
																	  unit_of_work=unit_of_work,
																	  sqlalchemy_session=sqlalchemy_session)
		self._student_presenter_composer = StudentPresenterComposer()

	def compose_course_push_control_api_controller(self):
		course_push_control_interactor = self._student_interactor_composer.compose_course_push_control_interactor()
		course_push_control_api_presenter = self._student_presenter_composer.compose_course_push_control_api_presenter()
		controller = CoursePushControlController(request=self._request,
										  		 course_push_control_interactor=course_push_control_interactor,
										   		 course_push_control_api_presenter=course_push_control_api_presenter)
		return ApiErrorHandlingControllerDecorator(controller)


	def compose_student_api_controller(self):
		student_interactor = self._student_interactor_composer.compose_student_interactor()
		controller = StudentApiController(request=self._request,
									student_interactor=student_interactor)
		return ApiErrorHandlingControllerDecorator(controller)

	def compose_student_course_api_controller(self):
		student_course_interactor = self._student_interactor_composer.compose_student_course_interactor()
		controller = StudentCourseApiController(request=self._request,
												student_course_interactor=student_course_interactor)
		return ApiErrorHandlingControllerDecorator(controller)
		
