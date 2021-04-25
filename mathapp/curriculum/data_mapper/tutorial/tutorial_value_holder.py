

class TutorialValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get(self):
		orm_tutorial = self._orm_model.tutorial
		if orm_tutorial is None:
			return None
		if not self._queried:
			self._unit_of_work.register_queried([orm_tutorial])
		tutorial = orm_tutorial.get_model(unit_of_work=self._unit_of_work)
		self._queried = True
		return tutorial

	def get_queried(self):
		return self._queried