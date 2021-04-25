from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial import tutorial_to_data

class TutorialInteractor:

	def __init__(self,
				 tutorial_factory,
				 lesson_repository,
				 unit_of_work):
		self._tutorial_factory = tutorial_factory
		self._lesson_repository = lesson_repository
		self._unit_of_work = unit_of_work

	def create(self, fields, lesson_id):
		lesson = self._lesson_repository.get(lesson_id)
		tutorial = self._tutorial_factory.create(fields=fields, lesson=lesson)
		self._unit_of_work.commit()
		return tutorial_to_data(tutorial)