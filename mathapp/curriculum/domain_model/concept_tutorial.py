from mathapp.curriculum.domain_model.lesson_section import LessonSection

from mathapp.library.errors.validation_error import ValidationError

class ConceptTutorial(LessonSection):

	def __init__(self, position, complete_lesson, display_name, parent_value_holder, unit_of_work):
		self._display_name = display_name
		self._unit_of_work = unit_of_work

		super().__init__(position, complete_lesson, parent_value_holder, unit_of_work)

		self._check_invariants()

	def _check_invariants(self):
		super()._check_invariants()
		if self._display_name is None:
			raise ValidationError(message = "Concept Tutorial requires display_name")

		if not self._display_name.strip():
			raise ValidationError(message = "Invalid display_name for Concept Tutorial")

		super()._check_invariants()

	def get_type(self):
		return 'concept_tutorial'

	def get_display_name(self):
		return self._display_name

	def __repr__(self):
		return f'<ConceptTutorial(id={self._id}, display_name={self._display_name})'