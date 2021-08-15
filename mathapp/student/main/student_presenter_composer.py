from mathapp.student.presenter.course_push_control_api_presenter import CoursePushControlApiPresenter
from mathapp.student.presenter.student_course_api_presenter import StudentCourseApiPresenter

class StudentPresenterComposer:

	def compose_course_push_control_api_presenter(self):
		return CoursePushControlApiPresenter()

	def compose_student_course_api_presenter(self):
		return StudentCourseApiPresenter()