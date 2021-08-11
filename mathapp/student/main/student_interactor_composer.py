from mathapp.student.main.student_repository_composer import StudentRepositoryComposer

from mathapp.student.interactor.course_push_control_interactor import CoursePushControlInteractor

class StudentInteractorComposer:

	def __init__(self,
				 unit_of_work,
				 sqlalchemy_session):
		self._unit_of_work = unit_of_work
		self._sqlalchemy_session = sqlalchemy_session
		self._student_repository_composer = StudentRepositoryComposer(unit_of_work=unit_of_work,
																	  sqlalchemy_session=sqlalchemy_session)

	def compose_course_push_control_interactor(self):
		course_push_control_repository = self._student_repository_composer.compose_course_push_control_repository()
		return CoursePushControlInteractor(course_push_control_repository=course_push_control_repository,
										   unit_of_work=self._unit_of_work)


