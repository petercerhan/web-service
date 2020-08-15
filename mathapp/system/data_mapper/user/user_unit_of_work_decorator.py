import weakref

class UserUnitOfWorkDecorator:

	def __init__(self, unit_of_work, orm_user):
		self._unit_of_work = unit_of_work
		self.orm_user = weakref.proxy(orm_user)

	def register_dirty(self, user):
		self._orm_user.sync_fields()

	def register_deleted(self, user):
		self._unit_of_work.register_deleted(self._orm_user)