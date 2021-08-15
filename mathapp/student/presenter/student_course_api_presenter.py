

class StudentCourseApiPresenter:

	def list(self, student_courses):
		envelope = {'data': student_courses}
		return envelope