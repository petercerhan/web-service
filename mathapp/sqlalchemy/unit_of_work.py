class UnitOfWork:

	def __init__(self, session):
		self._session = session
		self._mappers = []

	def register_created(self, mapper):
		self._mappers.append(mapper)
		self._session.add(mapper.get_orm_model())

	def register_deleted(self, mapper):
		self._session.delete(mapper.get_orm_model())

	def commit(self):
		self._session.commit()
		for mapper in self._mappers:
			mapper.sync_id()

	def register_queried(self, mappers):
		self._mappers.extend(mappers)
		