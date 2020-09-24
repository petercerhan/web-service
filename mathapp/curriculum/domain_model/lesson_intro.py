from mathapp.curriculum.domain_model.lesson_section import LessonSection

from mathapp.library.errors.validation_error import ValidationError

class LessonIntro(LessonSection):

	def __init__(self, position, complete_lesson, description):
		self._id = None

		self._description = description

		super().__init__(position, complete_lesson)

		self._check_invariants()

	def _check_invariants(self):
		if not self._description:
			raise ValidationError(message = "LessonIntro requires description")