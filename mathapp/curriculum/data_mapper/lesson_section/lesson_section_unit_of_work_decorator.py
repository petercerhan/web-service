import weakref

class LessonSectionUnitOfWorkDecorator:

	def __init__(self, unit_of_work, orm_lesson_section):
		self._unit_of_work = unit_of_work
		self._orm_lesson_section = weakref.proxy(orm_lesson_section)

	def register_dirty(self, lesson_section):
		self._orm_lesson_section.sync_fields()

	def register_deleted(self, lesson_section):
		self._unit_of_work.register_deleted(self._orm_lesson_section)