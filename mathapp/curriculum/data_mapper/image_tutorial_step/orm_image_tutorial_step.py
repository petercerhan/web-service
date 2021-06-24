from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.libraries.data_mapper_library.base import Base

from mathapp.curriculum.domain_model.image_tutorial_step import ImageTutorialStep
from mathapp.curriculum.data_mapper.tutorial_step.orm_tutorial_step import ORMTutorialStep

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMImageTutorialStep(ORMTutorialStep):
	__tablename__ = 'image_tutorial_step'
	id = Column(Integer, ForeignKey('tutorial_step.id'), primary_key=True)
	source_code_filename = Column(String)
	image_data = Column(LargeBinary)

	__mapper_args__ = {
		'polymorphic_identity': 'image_tutorial_step'
	}

	def __init__(self,
				 position,
				 display_group,
				 source_code_filename,
				 image_data):
		self.source_code_filename = source_code_filename
		self.image_data = image_data
		super().__init__(position=position, display_group=display_group)
		self._image_tutorial_step = None

	@orm.reconstructor
	def init_on_load(self):
		self._image_tutorial_step = None
		super().init_on_load()

	def get_model(self, unit_of_work):
		if self._image_tutorial_step is not None:
			return self._image_tutorial_step

		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

		image_tutorial_step = ImageTutorialStep(position=self.position,
												display_group=self.display_group,
												source_code_filename=self.source_code_filename,
												image_data=self.image_data,
												unit_of_work=domain_model_unit_of_work)
		image_tutorial_step._id = self.id
		self._image_tutorial_step = image_tutorial_step
		super()._set_model(image_tutorial_step)
		return image_tutorial_step

	def sync_id(self):
		self._image_tutorial_step._id = self.id

	def sync_fields(self):
		self.source_code_filename = self._image_tutorial_step._source_code_filename
		self.image_data = self._image_tutorial_step._image_data
		super().sync_fields()

	def __repr__(self):
		return f'<ORMImageTutorialStep(id={self.id}, type={self.type})>'






