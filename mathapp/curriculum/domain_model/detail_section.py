from mathapp.curriculum.domain_model.instruction_section import InstructionSection
from mathapp.library.errors.validation_error import ValidationError

class DetailSection(InstructionSection):

	def __init__(self, position, title, parent_value_holder, unit_of_work):
		self._title = title
		self._unit_of_work = unit_of_work

		super().__init__(position, parent_value_holder, unit_of_work)

		self._check_invariants()

	def _check_invariants(self):
		if not self._title:
			raise ValidationError(message = "DetailSection requires title")

		super()._check_invariants()

	def get_title(self):
		return self._title

	def set_title(self, title):
		self._title = title
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_type(self):
		return 'detail_section'

	def __repr__(self):
		return f'<DetailSection(id={self._id}, title={self._title})>'