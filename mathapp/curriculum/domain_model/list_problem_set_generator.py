from mathapp.curriculum.domain_model.problem_set_generator import ProblemSetGenerator
from mathapp.curriculum.domain_model.list_problem_set_dto_template import ListProblemSetDtoTemplate

class ListProblemSetGenerator(ProblemSetGenerator):

	def __init__(self,
				 name,
				 exercise_list_value_holder,
				 lesson_value_holder,
				 unit_of_work):
		self._unit_of_work = unit_of_work
		super().__init__(name, exercise_list_value_holder, lesson_value_holder, unit_of_work)

	def get_type(self):
		return 'list_problem_set_generator'

	def generate_problem_set(self, randomization_service, student_topic):
		exercises = self._exercise_list_value_holder.get_list()
		randomization_service.shuffle(exercises)
		return ListProblemSetDtoTemplate(exercises=exercises)


	def __repr__(self):
		return f'<ListProblemSetGenerator(id={self._id}, name={self._name})>'


