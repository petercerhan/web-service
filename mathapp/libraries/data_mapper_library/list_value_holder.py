

class ListValueHolder:

	def __init__(self, 
				 orm_model, 
				 property_name,
				 unit_of_work):
		self._orm_model = orm_model
		self._property_name = property_name
		self._unit_of_work = unit_of_work
		self._queried = False

	def get_list(self):
		orm_value_list = getattr(self._orm_model, self._property_name)
		if not self._queried:
			self._unit_of_work.register_queried(orm_value_list)
		value_list = [x.get_model(unit_of_work=self._unit_of_work) for x in orm_value_list]
		self._queried = True
		return value_list

	def remove_at_index(self, index):
		del getattr(self._orm_model, self._property_name)[index]

	def get_queried(self):
		return self._queried