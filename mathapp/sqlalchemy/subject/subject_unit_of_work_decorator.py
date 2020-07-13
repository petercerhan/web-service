import weakref

class SubjectUnitOfWorkDecorator:
	
	def __init__(self, unit_of_work, orm_subject):
		self._unit_of_work = unit_of_work
		self._orm_subject = weakref.proxy(orm_subject)

	def register_dirty(self, subject):
		self._orm_subject.sync_fields()

	def register_deleted(self, subject):
		self._unit_of_work.register_deleted(self._subject_mapper)
		