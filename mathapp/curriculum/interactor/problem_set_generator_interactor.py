from mathapp.curriculum.interactor.domain_to_data_transforms.problem_set_generator import problem_set_generator_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.list_problem_set_generator import list_problem_set_generator_to_enriched_data
from mathapp.curriculum.interactor.domain_to_data_transforms.exercise import exercise_to_data

class ProblemSetGeneratorInteractor:

	def __init__(self,
				 list_problem_set_generator_factory,
				 lesson_repository,
				 problem_set_generator_repository,
				 exercise_repository,
				 unit_of_work):
		self._list_problem_set_generator_factory = list_problem_set_generator_factory
		self._lesson_repository = lesson_repository
		self._problem_set_generator_repository = problem_set_generator_repository
		self._exercise_repository = exercise_repository
		self._unit_of_work = unit_of_work

	def get_list_problem_set_generator(self, id):
		list_problem_set_generator = self._problem_set_generator_repository.get(id=id)
		return list_problem_set_generator_to_enriched_data(list_problem_set_generator)

	def create_list_problem_set_generator(self, fields, lesson_id):
		lesson = self._lesson_repository.get(lesson_id)
		list_problem_set_generator = self._list_problem_set_generator_factory.create(fields=fields, lesson=lesson)
		self._unit_of_work.commit()
		return problem_set_generator_to_data(list_problem_set_generator)

	def update_list_problem_set_generator(self, id, fields):
		list_problem_set_generator = self._problem_set_generator_repository.get(id=id)
		name = fields.get('name')
		if name is not None:
			list_problem_set_generator.set_name(name)

		self._unit_of_work.commit()

		return list_problem_set_generator_to_enriched_data(list_problem_set_generator)

	def get_add_exercise_options(self, problem_set_generator_id):
		problem_set_generator = self._problem_set_generator_repository.get(id=problem_set_generator_id)
		add_exercise_options = problem_set_generator.get_add_exercise_options()
		options_data = [exercise_to_data(x) for x in add_exercise_options]
		return options_data

	def add_exercises_to_generator(self, problem_set_generator_id, exercise_id_list):
		problem_set_generator = self._problem_set_generator_repository.get(id=problem_set_generator_id)
		exercises = [self._exercise_repository.get(id=x) for x in exercise_id_list]
		for exercise in exercises:
			problem_set_generator.add_exercise(exercise)
		self._unit_of_work.commit()
		return problem_set_generator_to_data(problem_set_generator)
		