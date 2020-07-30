


class LessonSequenceItem:

	def __init__(self, position):
		self._id = None

		self._position = position

	def __repr__(self):
	return "<LessonSequenceItem(position='%s') Lesson(name='%s')>" % (self._position, self._lesson.name)