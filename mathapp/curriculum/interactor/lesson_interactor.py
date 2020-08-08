from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data


class LessonInteractor:
	
	def __init__(self, lesson_repository):
		self._lesson_repository = lesson_repository

	def list(self):
		lessons = self._lesson_repository.list()
		lessons_data = [lesson_to_data(lesson) for lesson in lessons]
		return lessons_data

	