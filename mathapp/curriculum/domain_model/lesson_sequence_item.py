from mathapp.library.errors.validation_error import ValidationError


class LessonSequenceItem:

	def __init__(self, position, lesson, unit_of_work):
		self._id = None

		self._position = position
		self._lesson = lesson

		self._unit_of_work = unit_of_work

		self._check_invariants()

	def _check_invariants(self):
		if self._position is None:
			raise ValidationError(message = "LessonSequenceItem requires position")

	def get_id(self):
		return self._id

	def get_position(self):
		return self._position

	def set_position(self, position):
		self._position = position
		self._unit_of_work.register_dirty(self)
		self._check_invariants

	def get_lesson(self):
		return self._lesson

	def __repr__(self):
		return "<LessonSequenceItem(position='%s') lesson(name='%s')>" % (self._position, self._lesson.get_name())