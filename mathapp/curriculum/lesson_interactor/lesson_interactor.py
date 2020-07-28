


class LessonInteractor:
	
	def __init__(self, lesson_repository):
		self._lesson_repository = lesson_repository

	def list(self):
		return self._lesson_repository.list()

	