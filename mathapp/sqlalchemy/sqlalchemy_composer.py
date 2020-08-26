from mathapp.sqlalchemy.db import Session
from mathapp.sqlalchemy.unit_of_work import UnitOfWork

class SQLAlchemyComposer:

	def __init__(self):
		self._session = None
		self._unit_of_work = None

	def compose_unit_of_work(self):
		if self._unit_of_work is None:
			session = self.compose_session()
			self._unit_of_work = UnitOfWork(self._session)
		return self._unit_of_work

	def compose_session(self):
		if self._session is None:
			self._session = Session()
		return self._session