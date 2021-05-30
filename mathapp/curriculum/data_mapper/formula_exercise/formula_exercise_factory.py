from mathapp.curriculum.data_mapper.formula_exercise.orm_formula_exercise import ORMFormulaExercise

class FormulaExerciseFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		tag = fields.get('tag')
		text = fields.get('text')
		formula_latex = fields.get('formula_latex')
		correct_option = fields.get('correct_option')
		incorrect_option_1 = fields.get('incorrect_option_1')
		incorrect_option_2 = fields.get('incorrect_option_2')
		incorrect_option_3 = fields.get('incorrect_option_3')
		orm_formula_exercise = ORMFormulaExercise(name=name,
												  tag=tag,
												  text=text,
												  formula_latex=formula_latex,
												  correct_option=correct_option,
												  incorrect_option_1=incorrect_option_1,
												  incorrect_option_2=incorrect_option_2,
												  incorrect_option_3=incorrect_option_3)
		formula_exercise = orm_formula_exercise.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_formula_exercise)
		return formula_exercise

