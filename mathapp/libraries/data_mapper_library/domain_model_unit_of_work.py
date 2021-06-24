import weakref

class DomainModelUnitOfWork:

	def __init__(self, unit_of_work, orm_model):
		self._unit_of_work = unit_of_work
		self._orm_model = weakref.proxy(orm_model)

	def register_dirty(self, model):
		self._orm_model.sync_fields()

	def register_deleted(self, model):
		self._unit_of_work.register_deleted(self._orm_model)