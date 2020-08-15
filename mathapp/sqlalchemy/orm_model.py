

class ORMModel:

	# Return the orm-independent model
	def get_model(self, unit_of_work):
		pass

	# Copy id field from orm_model to orm-independent model
	def sync_id(self):
		pass

	# Copy orm-independent model fields into orm_model
	def sync_fields(self):
		pass