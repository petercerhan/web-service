from mathapp.curriculum.data_mapper.formula_glyph.orm_formula_glyph import ORMFormulaGlyph

class FormulaGlyphFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields, position):
		formula = fields.get('formula')
		orm_formula_glyph = ORMFormulaGlyph(position=position, 
											formula=formula)
		formula_glyph = orm_formula_glyph.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_formula_glyph)
		return formula_glyph