from mathapp.curriculum.data_mapper.list_problem_set_generator.orm_list_problem_set_generator import ORMListProblemSetGenerator

class ListProblemSetGeneratorFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work
		
	def create(self, fields, lesson):
		orm_lesson = self._unit_of_work.orm_model_for_model(lesson)
		name = fields.get('name')
		orm_list_problem_set_generator = ORMListProblemSetGenerator(name=name)
		orm_lesson.problem_set_generator = orm_list_problem_set_generator

		list_problem_set_generator = orm_list_problem_set_generator.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_created(orm_list_problem_set_generator)
		return list_problem_set_generator