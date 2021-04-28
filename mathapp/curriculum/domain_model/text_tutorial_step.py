from mathapp.library.errors.validation_error import ValidationError
from mathapp.curriculum.domain_model.tutorial_step import TutorialStep

class TextTutorialStep(TutorialStep):

	def __init__(self,
				 position,
				 display_group,
				 text,
				 unit_of_work):
		self._text = text
		self._unit_of_work = unit_of_work
		super().__init__(position, display_group, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._text is None:
			raise ValidationError(message = "TextTutorialStep requires text")

		if not self._text.strip():
			raise ValidationError(message = f'Invalid text for TextTutorialStep (id={self._id})')

		super()._check_invariants()

	def get_type(self):
		return 'text_tutorial_step'

	def get_text(self):
		return self._text

	def __repr__(self):
		return f'<TextTutorialStep(id={self._id}, text={self._text})>'