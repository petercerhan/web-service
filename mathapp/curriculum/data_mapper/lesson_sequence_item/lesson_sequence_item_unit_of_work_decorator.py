import weakref

class LessonSequenceItemUnitOfWorkDecordator:

	def __init__(self, unit_of_work, orm_lesson_sequence_item):
		self._unit_of_work = unit_of_work
		self._orm_lesson_sequence_item = weakref.proxy(orm_lesson_sequence_item)

	def register_dirty(self, lesson_sequence_item):
		self._orm_lesson_sequence_item.sync_fields()

	def register_deleted(self, lesson):
		self._unit_of_work.register_deleted(self._orm_lesson_sequence_item)