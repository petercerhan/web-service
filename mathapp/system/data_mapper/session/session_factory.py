from mathapp.system.data_mapper.session.orm_session import ORMSession
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

import datetime

class SessionFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work
	
	def create(self, created_at):
		orm_session = ORMSession(revoked = False, created_at = created_at)

		session = orm_session.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_session)

		return session
