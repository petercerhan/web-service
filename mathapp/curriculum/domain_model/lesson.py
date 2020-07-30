from mathapp.library.errors.validation_error import ValidationError

class Lesson:

	def __init__(self, name, unit_of_work):
		self._id = None

		self._name = name
		if not name:
			raise ValidationError(message = "Subject requires name")

		self._unit_of_work = unit_of_work


	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def __repr__(self):
		return "<Lesson(name='%s') ID(id='%s')>" % (self._name, self._id)