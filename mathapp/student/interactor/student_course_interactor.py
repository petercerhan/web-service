from mathapp.student.interactor.domain_to_data_transforms.student_course import student_course_to_enriched_data
from mathapp.student.interactor.domain_to_data_transforms.student_course import student_course_to_data

class StudentCourseInteractor:

	def __init__(self,
				 student_course_repository,
				 student_topic_factory,
				 unit_of_work):
		self._student_course_repository = student_course_repository
		self._student_topic_factory = student_topic_factory
		self._unit_of_work = unit_of_work

	def get(self, student_course_id):
		student_course = self._student_course_repository.get(student_course_id=student_course_id)
		return student_course_to_enriched_data(student_course)

	def list(self):
		student_courses = self._student_course_repository.list()
		student_courses_data = [student_course_to_data(x) for x in student_courses]
		return student_courses_data

	def sync_latest_course_push(self, student_course_id):
		student_course = self._student_course_repository.get(student_course_id=student_course_id)
		student_course.sync_latest_course_push(student_topic_factory=self._student_topic_factory)
		self._unit_of_work.commit()
		return student_course_to_enriched_data(student_course)

