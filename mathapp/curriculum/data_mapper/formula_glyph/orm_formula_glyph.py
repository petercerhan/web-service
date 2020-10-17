from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.formula_glyph import FormulaGlyph
from mathapp.curriculum.data_mapper.detail_glyph.orm_detail_glyph import ORMDetailGlyph

class ORMFormulaGlyph(ORMDetailGlyph):
	__tablename__ = 'formula_glyph'
	id = Column(Integer, ForeignKey('detail_glyph.id'), primary_key=True)
	formula = Column(String)

	__mapper_args__ = {
		'polymorphic_identity': 'formula_glyph'
	}

	def __init__(self, position, formula):
		self.formula = formula
		super().__init__(position)
		self._formula_glyph = None

	@orm.reconstructor
	def init_on_load(self):
		self._formula_glyph = None
		super().init_on_load()

	def get_model(self, unit_of_work):
		if self._formula_glyph is not None:
			return self._formula_glyph

		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

		formula_glyph = FormulaGlyph(position=self.position, 
									 formula=self.formula, 
									 unit_of_work=domain_model_unit_of_work)
		formula_glyph._id = self.id
		self._formula_glyph = formula_glyph
		super()._set_model(formula_glyph)
		return formula_glyph

	def sync_id(self):
		self._formula_glyph._id = self.id

	def sync_fields(self):
		self.formula = self._formula_glyph._formula
		super().sync_fields()

	def __repr__(self):
		return f'<ORMFormulaGlyph(id={self.id}, type={self.type})>'


