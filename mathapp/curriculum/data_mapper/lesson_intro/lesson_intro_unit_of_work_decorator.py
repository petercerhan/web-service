import weakref

class LessonIntroUnitOfWorkDecorator:

	def __init__(self, unit_of_work, orm_lesson_intro):
		self._unit_of_work = unit_of_work
		self._orm_lesson_intro = weakref.proxy(orm_lesson_intro)

	def register_dirty(self, lesson_intro):
		self._orm_lesson_intro.sync_fields()

	def register_deleted(self, lesson_intro):
		self._unit_of_work.register_deleted(self._orm_lesson_intro)

