

class LessonSequenceItemListValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get_list(self):
		orm_lesson_sequence_items = self._orm_model.lesson_sequence_items
		if not self._queried:
			self._unit_of_work.register_queried(orm_lesson_sequence_items)
		lesson_sequence_items = [orm_item.get_model(unit_of_work=self._unit_of_work) for orm_item in orm_lesson_sequence_items]
		self._queried = True
		return lesson_sequence_items

	def add(self, lesson_sequence_item):
		orm_lesson_sequence_item = self._unit_of_work.orm_model_for_model(lesson_sequence_item)
		self._orm_model.lesson_sequence_items.append(orm_lesson_sequence_item)

	def removeAtIndex(self, index):
		del self._orm_model.lesson_sequence_items[index]

	def get_queried(self):
		return self._queried