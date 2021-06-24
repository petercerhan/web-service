from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.curriculum.domain_model.tutorial_step import TutorialStep

class FormulaTutorialStep(TutorialStep):

	def __init__(self,
				 position,
				 display_group,
				 formula_latex,
				 unit_of_work):
		self._formula_latex = formula_latex
		self._unit_of_work = unit_of_work
		super().__init__(position, display_group, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._formula_latex is None:
			raise ValidationError(message = "FormulaTutorialStep requires formula_latex")

		if not self._formula_latex.strip():
			raise ValidationError(message = f'Invalid formula_latex for FormulaTutorialStep (id={self._id})')

		super()._check_invariants()

	def get_type(self):
		return 'formula_tutorial_step'

	def get_formula_latex(self):
		return self._formula_latex

	def set_formula_latex(self, formula_latex):
		self._formula_latex = formula_latex
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def __repr__(self):
		return f'<FormulaTutorialStep(id={self._id}, formula_latex={self._formula_latex})>'