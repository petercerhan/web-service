from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError

class LessonRepository:

	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def get(self, id):
		orm_lesson = self._session.query(ORMLesson).filter(ORMLesson.id == id).first()

		if not orm_lesson:
			raise NotFoundError(message=f'Lesson id={id} not found')

		lesson = orm_lesson.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_lesson])
		return lesson

	