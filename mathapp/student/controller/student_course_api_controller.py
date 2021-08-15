

class StudentCourseApiController:

	def __init__(self,
				 request,
				 student_course_interactor):
		self._request = request
		self._student_course_interactor = student_course_interactor

	def get(self, student_course_id):
		return self._student_course_interactor.get(student_course_id=student_course_id)

