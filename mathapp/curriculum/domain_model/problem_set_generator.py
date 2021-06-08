from mathapp.library.errors.validation_error import ValidationError

class ProblemSetGenerator:

	def __init__(self,
				 name,
				 exercise_list_value_holder,
				 unit_of_work):
		self._id = None
		self._name = name
		self._exercise_list_value_holder = exercise_list_value_holder
		self._unit_of_work = unit_of_work
		self._check_invariants()

	def _check_invariants(self):
		if self._name is None:
			raise ValidationError(message = f'ProblemSetGenerator requires name (id={self._id})')

		if self._name.strip() == '':
			raise ValidationError(message = f'ProblemSetGenerator requires name (id={self._id})')

	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def __repr__(self):
		return f'<ProblemSetGenerator(id={self._id}, name={self._name})>'


