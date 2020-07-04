from mathapp.db_sqlalchemy import Session

class UnitOfWork:

	def __init__(self):
		self._mappers = []

	def register_created(self, mapper):
		self._mappers.append(mapper)
		Session.add(mapper.get_orm_model())

	def commit(self):
		Session.commit()
		for mapper in self._mappers:
			mapper.sync_id()

	def register_queried(self, mappers):
		self._mappers.extend(mappers)
		