


class LessonSequenceItem:

	def __init__(self, position, lesson, unit_of_work):
		self._id = None

		self._position = position
		self._lesson = lesson

		self._unit_of_work = unit_of_work

	def get_lesson(self):
		return self._lesson

	def __repr__(self):
		return "<LessonSequenceItem(position='%s') lesson(name='%s')>" % (self._position, self._lesson.get_name())