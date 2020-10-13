from mathapp.library.errors.validation_error import ValidationError

class InstructionSection:

	def __init__(self, position, unit_of_work):
		self._id = None
		self._position = position
		self._unit_of_work = unit_of_work
		self._check_invariants()

	def _check_invariants(self):
		if self._position is None:
			raise ValidationError(message = "InstructionSection requires position")

	def get_id(self):
		return self._id

	def get_position(self):
		return self._position

	def set_position(self, position):
		self._position = position
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_type(self):
		return 'instruction_section'


	def __repr__(self):
		return f'<InstructionSection(id={self._id})>'