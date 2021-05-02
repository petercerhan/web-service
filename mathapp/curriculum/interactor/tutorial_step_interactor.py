from mathapp.curriculum.interactor.domain_to_data_transforms.text_tutorial_step import text_tutorial_step_to_data

class TutorialStepInteractor:

	def __init__(self,
				 tutorial_repository,
				 text_tutorial_step_factory,
				 formula_tutorial_step_factory,
				 unit_of_work):
		self._tutorial_repository = tutorial_repository
		self._text_tutorial_step_factory = text_tutorial_step_factory
		self._formula_tutorial_step_factory = formula_tutorial_step_factory
		self._unit_of_work = unit_of_work

	def create_text_tutorial_step(self, tutorial_id, fields):
		tutorial = self._tutorial_repository.get(tutorial_id)
		text_tutorial_step = tutorial.create_tutorial_step(self._text_tutorial_step_factory, fields)
		self._unit_of_work.commit()
		return text_tutorial_step_to_data(text_tutorial_step)