import weakref

class SubjectUnitOfWorkDecorator:
	
	def __init__(self, unit_of_work, subject_mapper):
		self._unit_of_work = unit_of_work
		self._subject_mapper = weakref.proxy(subject_mapper)

	def register_dirty(self, subject):
		self._subject_mapper.sync_orm_model()

	def register_deleted(self, subject):
		self._unit_of_work.register_deleted(self._subject_mapper)