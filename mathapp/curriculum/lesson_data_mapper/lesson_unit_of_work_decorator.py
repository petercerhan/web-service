import weakref

class LessonUnitOfWorkDecorator:
	
	def __init__(self, unit_of_work, orm_lesson):
		self._unit_of_work = unit_of_work
		self._orm_lesson = weakref.proxy(orm_lesson)

	def register_dirty(self, lesson):
		self._orm_lesson.sync_fields()

	def register_deleted(self, lesson):
		self._unit_of_work.register_deleted(self._orm_lesson)