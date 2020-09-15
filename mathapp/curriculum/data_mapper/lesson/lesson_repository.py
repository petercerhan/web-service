from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson
from mathapp.library.errors.not_found_error import NotFoundError

class LessonRepository:
	
	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def list(self):
		orm_lessons = self._session.query(ORMLesson).all()
		lessons = [orm_lesson.get_model(unit_of_work=self._unit_of_work) for orm_lesson in orm_lessons]
		self._unit_of_work.register_queried(orm_lessons)
		return lessons

	def get_by_name(self, name):
		orm_lesson = self._session.query(ORMLesson).filter(ORMLesson.name == name).first()

		if not orm_lesson:
			raise NotFoundError(message='Not Found')

		lesson = orm_lesson.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_lesson])

		return lesson