

class StudentCourseApiController:

	def __init__(self,
				 request,
				 student_course_interactor,
				 student_course_api_presenter):
		self._request = request
		self._student_course_interactor = student_course_interactor
		self._student_course_api_presenter = student_course_api_presenter

	def get(self, student_course_id):
		return self._student_course_interactor.get(student_course_id=student_course_id)

	def list(self):
		student_courses = self._student_course_interactor.list()
		return self._student_course_api_presenter.list(student_courses)

	def sync_latest_course_push(self, student_course_id):
		return self._student_course_interactor.sync_latest_course_push(student_course_id=student_course_id)

