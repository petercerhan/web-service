from mathapp.curriculum.domain_model.detail_glyph import DetailGlyph

class FormulaGlyph(DetailGlyph):

	def __init__(self, position, formula, unit_of_work):
		self._formula = formula
		self._unit_of_work = unit_of_work
		super().__init__(position, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._formula is None:
			raise ValidationError(message = f'FormulaGlyph (id={self._id}) requires formula')

		if not self._formula.strip():
			raise ValidationError(message = f'Invalid formula for FormulaGlyph (id={self._id})')

		super()._check_invariants()

	def get_formula(self):
		return self._formula

	def get_type(self):
		return 'formula_glyph'

	def __repr__(self):
		return f'<FormulaGlyph(id={self._id}, formula={self._formula})>'