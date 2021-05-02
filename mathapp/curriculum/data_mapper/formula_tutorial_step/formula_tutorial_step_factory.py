from mathapp.curriculum.data_mapper.formula_tutorial_step.orm_formula_tutorial_step import ORMFormulaTutorialStep

class FormulaTutorialStepFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields, position, display_group):
		formula_latex = fields.get('formula_latex')
		orm_formula_tutorial_step = ORMFormulaTutorialStep(position=position,
														   display_group=display_group,
														   formula_latex=formula_latex)
		formula_tutorial_step = orm_formula_tutorial_step.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_formula_tutorial_step)
		return formula_tutorial_step

