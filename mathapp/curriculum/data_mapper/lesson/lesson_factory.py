from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson

class LessonFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		orm_lesson = ORMLesson(name=name)

		lesson = orm_lesson.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_lesson)

		return lesson