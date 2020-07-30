


class LessonSequenceItem:

	def __init__(self, position, unit_of_work):
		self._id = None

		self._position = position

		self._unit_of_work = unit_of_work

	def __repr__(self):
		return "<LessonSequenceItem(position='%s') id(id='%s')>" % (self._position, self._id)