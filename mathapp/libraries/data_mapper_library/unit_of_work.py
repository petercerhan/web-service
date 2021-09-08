import sys

class UnitOfWork:

	def __init__(self, session):
		self._session = session
		self._orm_models = []

	def register_created(self, orm_model):
		self._orm_models.append(orm_model)
		self._session.add(orm_model)

	def register_deleted(self, orm_model):
		self._session.delete(orm_model)

	def commit(self):
		self._session.commit()
		for orm_model in self._orm_models:
			orm_model.sync_id()

	def register_queried(self, orm_models):
		self._orm_models.extend(orm_models)
	
	def orm_model_for_model(self, model):
		for orm_model in self._orm_models:
			if orm_model.get_model(unit_of_work=self) is model:
				return orm_model