import weakref

class CourseUnitOfWorkDecorator:
	
	def __init__(self, unit_of_work, orm_course):
		self._unit_of_work = unit_of_work
		self._orm_course = weakref.proxy(orm_course)

	def register_dirty(self, course):
		self._orm_course.sync_fields()

	def register_deleted(self, course):
		self._unit_of_work.register_deleted(self._orm_course)
		