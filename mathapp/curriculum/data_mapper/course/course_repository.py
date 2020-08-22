from mathapp.curriculum.data_mapper.course.orm_course import ORMCourse
from mathapp.library.errors.not_found_error import NotFoundError

class CourseRepository:

	def __init__(self, unit_of_work, session):
		self._session = session
		self._unit_of_work = unit_of_work
	
	def list(self):
		orm_courses = self._session.query(ORMCourse).all()
		courses = [orm_course.get_model(unit_of_work=self._unit_of_work) for orm_course in orm_courses]
		self._unit_of_work.register_queried(orm_courses)
		return courses

	def get(self, id):
		orm_course = self._session.query(ORMCourse).filter(ORMCourse.id == id).first()

		if not orm_course:
			raise NotFoundError(message = "Not Found")

		course = orm_course.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_course])

		return course

	def get_by_name(self, name):
		orm_course = self._session.query(ORMCourse).filter(ORMCourse.name == name).first()

		if not orm_course:
			raise NotFoundError(message = "Not Found")

		course = orm_course.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_course])

		return course