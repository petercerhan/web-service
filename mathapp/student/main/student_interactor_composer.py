from mathapp.student.main.student_repository_composer import StudentRepositoryComposer

from mathapp.student.interactor.course_push_control_interactor import CoursePushControlInteractor
from mathapp.student.interactor.student_interactor import StudentInteractor

class StudentInteractorComposer:

	def __init__(self,
				 user_data,
				 unit_of_work,
				 sqlalchemy_session):
		self._unit_of_work = unit_of_work
		self._sqlalchemy_session = sqlalchemy_session
		self._student_repository_composer = StudentRepositoryComposer(user_data=user_data,
																	  unit_of_work=unit_of_work,
																	  sqlalchemy_session=sqlalchemy_session)

	def compose_course_push_control_interactor(self):
		course_push_control_repository = self._student_repository_composer.compose_course_push_control_repository()
		return CoursePushControlInteractor(course_push_control_repository=course_push_control_repository,
										   unit_of_work=self._unit_of_work)

	def compose_student_interactor(self):
		student_course_repository = self._student_repository_composer.compose_student_course_repository()
		return StudentInteractor(student_course_repository=student_course_repository,
								 unit_of_work=self._unit_of_work)
