

class ValueHolder:

	def __init__(self, 
				 orm_model, 
				 property_name,
				 set_at_init,
				 unit_of_work):
		self._orm_model = orm_model
		self._property_name = property_name
		self._set_at_init = set_at_init
		self._unit_of_work = unit_of_work
		self._queried = False

	def get(self):
		orm_value = getattr(self._orm_model, self._property_name)
		if orm_value is None:
			return None
		if not self._queried:
			self._unit_of_work.register_queried([orm_value])
		value = orm_value.get_model(unit_of_work=self._unit_of_work)
		self._queried = True
		return value

	def set(self, model_to_set):
		orm_model_to_set = self._unit_of_work.orm_model_for_model(model_to_set)
		setattr(self._orm_model, self._property_name, orm_model_to_set)


	def get_set_at_init(self):
		return self._set_at_init

	def get_queried(self):
		return self._queried