from mathapp.curriculum.domain_model.instruction_section import InstructionSection
from mathapp.library.errors.validation_error import ValidationError

class DerivationInstructionSection(InstructionSection):

	def __init__(self, position, display_name, parent_value_holder, unit_of_work):
		self._display_name = display_name
		self._unit_of_work = unit_of_work
		super().__init__(position, parent_value_holder, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if not self._display_name:
			raise ValidationError(message = "DerivationInstructionSection requires title")

		super()._check_invariants()

	def get_display_name(self):
		return self._display_name

	def get_type(self):
		return 'derivation_instruction_section'

	def __repr__(self):
		return f'<DerivationInstructionSection(id={self._id}, display_name={self._display_name})>'
