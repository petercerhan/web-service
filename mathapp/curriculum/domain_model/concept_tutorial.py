from mathapp.curriculum.domain_model.lesson_section import LessonSection

from mathapp.library.errors.validation_error import ValidationError

class ConceptTutorial:

	def __init__(self, position, complete_lesson, display_name, unit_of_work):
		self._display_name = display_name
		self._unit_of_work = unit_of_work

		super().__init__(position, complete_lesson)

		self._check_invariants()

	def _check_invariants(self):
		if not self._display_name:
			raise ValidationError(message = "ConceptTutorial requires display_name")

	def __repr__(self):
		return f'<ConceptTutorial(id={self._id}, display_name={self._display_name})'