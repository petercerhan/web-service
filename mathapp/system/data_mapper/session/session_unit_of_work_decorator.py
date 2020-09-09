import weakref

class SessionUnitOfWorkDecorator:
	
	def __init__(self, unit_of_work, orm_session):
		self._unit_of_work = unit_of_work
		self._orm_session = weakref.proxy(orm_session)

	def register_dirty(self, session):
		self._orm_session.sync_fields()

	def register_deleted(self, session):
		self._unit_of_work.register_deleted(self._session)