from mathapp.library.errors.validation_error import ValidationError

class TutorialStep:

	def __init__(self, 
				 position,
				 display_group,
				 unit_of_work):
		self._id = None
		self._position = position
		self._display_group = display_group
		self._unit_of_work = unit_of_work
		self._check_invariants()

	def _check_invariants(self):
		if self._position is None:
			raise ValidationError(message = "TutorialStep requires position")

		if self._display_group is None:
			raise ValidationError(message = "TutorialStep requires display_group")

	def get_type(self):
		return 'tutorial_step'

	def get_id(self):
		return self._id

	def get_position(self):
		return self._position

	def get_display_group(self):
		return self._display_group

	def __repr__(self):
		return f'<TutorialStep(id={self._id})>'

