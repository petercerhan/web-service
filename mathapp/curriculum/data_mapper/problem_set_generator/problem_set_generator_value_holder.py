

class ProblemSetGeneratorValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get(self):
		orm_problem_set_generator = self._orm_model.problem_set_generator
		if orm_problem_set_generator is None:
			return None
		if not self._queried:
			self._unit_of_work.register_queried([orm_problem_set_generator])
		problem_set_generator = orm_problem_set_generator.get_model(unit_of_work=self._unit_of_work)
		self._queried = True
		return problem_set_generator

	def get_queried(self):
		return self._queried
