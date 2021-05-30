

class ExerciseListValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get_list(self):
		orm_exercises = self._orm_model.exercises
		if not self._queried:
			self._unit_of_work.register_queried(orm_exercises)
		exercises = [x.get_model(unit_of_work=self._unit_of_work) for x in orm_exercises]
		self._queried = True
		return exercises

	def add(self, exercise):
		orm_exercise = self._unit_of_work.orm_model_for_model(exercise)
		self._orm_model.exercises.append(orm_exercise)

	def remove_at_index(self, index):
		del self._orm_model.exercises[index]

	def get_queried(self):
		return self._queried


