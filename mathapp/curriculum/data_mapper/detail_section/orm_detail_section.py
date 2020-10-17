from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.detail_section import DetailSection
from mathapp.curriculum.data_mapper.instruction_section.orm_instruction_section import ORMInstructionSection

from mathapp.curriculum.data_mapper.instruction_section.instruction_section_parent_value_holder import InstructionSectionParentValueHolder

from mathapp.curriculum.data_mapper.detail_glyph.orm_detail_glyph import ORMDetailGlyph
from mathapp.curriculum.data_mapper.text_glyph.orm_text_glyph import ORMTextGlyph
from mathapp.curriculum.data_mapper.formula_glyph.orm_formula_glyph import ORMFormulaGlyph
from mathapp.curriculum.data_mapper.detail_glyph.detail_glyph_list_value_holder import DetailGlyphListValueHolder

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMDetailSection(ORMInstructionSection):
	__tablename__ = 'detail_section'
	id = Column(Integer, ForeignKey('instruction_section.id'), primary_key=True)
	title = Column(String)

	detail_glyphs = relationship('ORMDetailGlyph', order_by='asc(ORMDetailGlyph.position)')

	__mapper_args__ = {
		'polymorphic_identity': 'detail_section'
	}

	def __init__(self, position, title):
		self.title = title
		super().__init__(position)
		self._detail_section = None

	@orm.reconstructor
	def init_on_load(self):
		self._detail_section = None
		super().init_on_load()

	def get_model(self, unit_of_work):
		if self._detail_section is not None:
			return self._detail_section

		parent_value_holder = InstructionSectionParentValueHolder(orm_instruction_section=self, unit_of_work=unit_of_work)
		detail_glyph_list_value_holder = DetailGlyphListValueHolder(orm_model=self, unit_of_work=unit_of_work)
		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

		detail_section = DetailSection(position=self.position, 
										title=self.title, 
										parent_value_holder=parent_value_holder, 
										detail_glyph_list_value_holder=detail_glyph_list_value_holder,
										unit_of_work=domain_model_unit_of_work)
		detail_section._id = self.id

		self._detail_section = detail_section
		super()._set_model(detail_section)
		return detail_section

	def sync_id(self):
		self._detail_section._id = self.id

	def sync_fields(self):
		self.title = self._detail_section._title
		super().sync_fields()

	def __repr__(self):
		return f'<ORMDetailSection(id={self.id}, title={self.title})>'

