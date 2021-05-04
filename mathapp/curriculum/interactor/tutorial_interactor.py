from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial import tutorial_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial import tutorial_to_enriched_data

class TutorialInteractor:

	def __init__(self,
				 tutorial_factory,
				 tutorial_repository,
				 lesson_repository,
				 unit_of_work):
		self._tutorial_factory = tutorial_factory
		self._tutorial_repository = tutorial_repository
		self._lesson_repository = lesson_repository
		self._unit_of_work = unit_of_work

	def create(self, fields, lesson_id):
		lesson = self._lesson_repository.get(lesson_id)
		tutorial = self._tutorial_factory.create(fields=fields, lesson=lesson)
		self._unit_of_work.commit()
		return tutorial_to_enriched_data(tutorial)

	def get(self, id):
		tutorial = self._tutorial_repository.get(id)
		return tutorial_to_enriched_data(tutorial)

	def update(self, id, fields):
		tutorial = self._tutorial_repository.get(id)

		name = fields.get('name')
		if name is not None:
			tutorial.set_name(name)

		tutorial_steps = fields.get('tutorial_steps')
		if tutorial_steps is not None:
			tutorial.sync_tutorial_step_positions(tutorial_steps_data_array=tutorial_steps)

		self._unit_of_work.commit()
		return tutorial_to_enriched_data(tutorial)

	def delete(self, id):
		tutorial = self._tutorial_repository.get(id)
		tutorial.delete()
		self._unit_of_work.commit()
		return id
		
