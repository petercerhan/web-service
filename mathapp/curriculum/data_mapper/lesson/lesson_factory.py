from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson

class LessonFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, position, fields, topic):
		name = fields.get('name')
		orm_lesson = ORMLesson(name=name, position=position)

		orm_topic = self._unit_of_work.orm_model_for_model(topic)
		orm_topic.lessons.append(orm_lesson)

		lesson = orm_lesson.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_created(orm_lesson)

		return lesson