from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data

class LessonInteractor:

	def __init__(self,
				 lesson_repository,
				 unit_of_work):
		self._lesson_repository = lesson_repository
		self._unit_of_work = unit_of_work

	def get(self, id):
		lesson = self._lesson_repository.get(id)
		return lesson_to_data(lesson)
