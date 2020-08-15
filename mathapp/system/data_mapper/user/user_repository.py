from mathapp.system.data_mapper.user.orm_user import ORMUser
from mathapp.library.errors.not_found_error import NotFoundError

class UserRepository:


	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def get(self, id):
		orm_user = self._session.query(ORMUser).filter(ORMUser.id == id).first()

		if not orm_user:
			raise NotFoundError(message = "User Not Found")

		##To do - set up model user
		##Register model user queried

		return orm_user

	def get_by_username(self, username):
		orm_user = self._session.query(ORMUser).filter(ORMUser.username == username).first()

		if not orm_user:
			raise NotFoundError(message = "User Not Found")

		return orm_user