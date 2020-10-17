from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.text_glyph import TextGlyph
from mathapp.curriculum.data_mapper.detail_glyph.orm_detail_glyph import ORMDetailGlyph

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMTextGlyph(ORMDetailGlyph):
	__tablename__ = 'text_glyph'
	id = Column(Integer, ForeignKey('detail_glyph.id'), primary_key=True)
	text = Column(String)

	__mapper_args__ = {
		'polymorphic_identity': 'text_glyph'
	}

	def __init__(self, position, text):
		self.text = text
		super().__init__(position)
		self._text_glyph = None

	@orm.reconstructor
	def init_on_load(self):
		self._text_glyph = None
		super().init_on_load()

	def get_model(self, unit_of_work):
		if self._text_glyph is not None:
			return self._text_glyph

		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

		text_glyph = TextGlyph(position=self.position, 
							   text=self.text, 
							   unit_of_work=domain_model_unit_of_work)
		text_glyph._id = self.id
		self._text_glyph = text_glyph
		super()._set_model(text_glyph)
		return text_glyph

	def sync_id(self):
		self._text_glyph._id = self.id

	def sync_fields(self):
		self.text = self._text_glyph._text
		super().sync_fields()

	def __repr__(self):
		return f'<ORMTextGlyph(id={self.id}, type={self.type})>'