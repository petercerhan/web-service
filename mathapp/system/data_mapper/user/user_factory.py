from mathapp.system.data_mapper.user.orm_user import ORMUser

class UserFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		username = fields.get('username')
		password = fields.get('password')
		orm_user = ORMUser(username = username, password = password)

		user = orm_user.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_user)

		return user

