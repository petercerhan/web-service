from mathapp.system.data_mapper.session.orm_session import ORMSession
from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError

import datetime

class SessionFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work
	
	def create(self, user, created_at):
		orm_session = ORMSession(user_id = user.get_id(),
								revoked = False, 
								created_at = created_at)

		session = orm_session.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_session)

		return session
