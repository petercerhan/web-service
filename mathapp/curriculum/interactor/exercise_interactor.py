from mathapp.curriculum.interactor.domain_to_data_transforms.exercise import exercise_to_data

class ExerciseInteractor:

	def __init__(self,
				 topic_repository,
				 formula_exercise_factory,
				 unit_of_work):
		self._topic_repository = topic_repository
		self._formula_exercise_factory = formula_exercise_factory
		self._unit_of_work = unit_of_work

	def create_formula_exercise(self, topic_id, fields):
		topic = self._topic_repository.get(id=topic_id)
		formula_exercise = topic.create_exercise(exercise_factory=self._formula_exercise_factory, fields=fields)
		self._unit_of_work.commit()
		return exercise_to_data(formula_exercise)