from mathapp.curriculum.data_mapper.lesson_sequence_item.orm_lesson_sequence_item import ORMLessonSequenceItem


class LessonSequenceItemFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, position, lesson):
		orm_lesson = self._unit_of_work.orm_model_for_model(lesson)
		orm_lesson_sequence_item = ORMLessonSequenceItem(position=position)
		orm_lesson_sequence_item.lesson = orm_lesson

		lesson_sequence_item = orm_lesson_sequence_item.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_created(orm_lesson_sequence_item)

		return lesson_sequence_item