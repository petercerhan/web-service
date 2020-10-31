from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.image_glyph import ImageGlyph
from mathapp.curriculum.data_mapper.detail_glyph.orm_detail_glyph import ORMDetailGlyph

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMImageGlyph(ORMDetailGlyph):
	__tablename__ = 'image_glyph'
	id = Column(Integer, ForeignKey('detail_glyph.id'), primary_key=True)
	source_code_filename = Column(String)
	image_data = Column(LargeBinary)

	__mapper_args__ = {
		'polymorphic_identity': 'image_glyph'
	}

	def __init__(self, position, source_code_filename, image_data):
		self.source_code_filename = source_code_filename
		self.image_data = image_data
		super().__init__(position)
		self._image_glyph = None

	@orm.reconstructor
	def init_on_load(self):
		self._image_glyph = None
		super().init_on_load()

	def get_model(self, unit_of_work):
		if self._image_glyph is not None:
			return self._image_glyph

		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

		image_glyph = ImageGlyph(position=self.position, 
								 source_code_filename=self.source_code_filename, 
								 image_data=self.image_data,
								 unit_of_work=domain_model_unit_of_work)
		image_glyph._id = self.id
		self._image_glyph = image_glyph
		super()._set_model(image_glyph)
		return image_glyph

	def sync_id(self):
		self._image_glyph._id = self.id

	def sync_fields(self):
		self.source_code_filename = self._image_glyph._source_code_filename
		self.image_data = self._image_glyph._image_data
		super().sync_fields()

	def __repr__(self):
		return f'<ORMImageGlyph(id={self.id}, type={self.type})>'