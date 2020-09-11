

class UserValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get(self):
		orm_user = self._orm_model.user
		user = orm_user.get_model(unit_of_work=self._unit_of_work)
		self._queried = True
		return user

	def get_queried(self):
		return self._queried
