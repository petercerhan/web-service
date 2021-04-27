

class TutorialStepListValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get_list(self):
		orm_tutorial_steps = self._orm_model.tutorial_steps
		if not self._queried:
			self._unit_of_work.register_queried(orm_tutorial_steps)
		tutorial_steps = [x.get_model(unit_of_work=self._unit_of_work) for x in orm_tutorial_steps]
		self._queried = True
		return tutorial_steps

	def add(self, tutorial_step):
		orm_tutorial_step = self._unit_of_work.orm_model_for_model(tutorial_step)
		self._orm_model.tutorial_steps.append(orm_tutorial_step)

	def remove_at_index(self, index):
		del self._orm_model.tutorial_steps[index]

	def get_queried(self):
		return self._queried