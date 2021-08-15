from mathapp.student.interactor.domain_to_data_transforms.student_course import student_course_to_enriched_data

class StudentCourseInteractor:

	def __init__(self,
				 student_course_repository):
		self._student_course_repository = student_course_repository

	def get(self, student_course_id):
		student_course = self._student_course_repository.get(student_course_id=student_course_id)
		return student_course_to_enriched_data(student_course)
