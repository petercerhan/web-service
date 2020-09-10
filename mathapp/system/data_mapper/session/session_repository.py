from mathapp.system.data_mapper.session.orm_session import ORMSession
from mathapp.library.errors.not_found_error import NotFoundError

class SessionRepository:

	def __init__(self, unit_of_work, sqlalchemy_session):
		self._unit_of_work = unit_of_work
		self._sqlalchemy_session = sqlalchemy_session

	def get(self, id):
		orm_session = self._sqlalchemy_session.query(ORMSession).filter(ORMSession.id == id).first()

		if not orm_session:
			raise NotFoundError(message = "Session Not Found")

		session = orm_session.get_model(unit_of_work = self._unit_of_work)
		self._unit_of_work.register_queried([orm_session])

		return session