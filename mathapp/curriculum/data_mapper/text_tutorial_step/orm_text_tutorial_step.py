from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.libraries.data_mapper_library.base import Base

from mathapp.curriculum.domain_model.text_tutorial_step import TextTutorialStep
from mathapp.curriculum.data_mapper.tutorial_step.orm_tutorial_step import ORMTutorialStep

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMTextTutorialStep(ORMTutorialStep):
	__tablename__ = 'text_tutorial_step'
	id = Column(Integer, ForeignKey('tutorial_step.id'), primary_key=True)
	text = Column(String)

	__mapper_args__ = {
		'polymorphic_identity': 'text_tutorial_step'
	}

	def __init__(self,
				 position,
				 display_group,
				 text,
				 tutorial_id):
		self.text = text
		super().__init__(position=position, 
						 display_group=display_group,
						 tutorial_id=tutorial_id)
		self._text_tutorial_step = None

	@orm.reconstructor
	def init_on_load(self):
		self._text_tutorial_step = None
		super().init_on_load()

	def get_model(self, unit_of_work):
		if self._text_tutorial_step is not None:
			return self._text_tutorial_step

		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

		text_tutorial_step = TextTutorialStep(position=self.position,
											  display_group=self.display_group,
											  text=self.text,
											  unit_of_work=domain_model_unit_of_work)
		text_tutorial_step._id = self.id
		self._text_tutorial_step = text_tutorial_step
		super()._set_model(text_tutorial_step)
		return text_tutorial_step

	def sync_id(self):
		self._text_tutorial_step._id = self.id

	def sync_fields(self):
		self.text = self._text_tutorial_step._text 
		super().sync_fields()

	def __repr__(self):
		return f'<ORMTextTutorialStep(id={self.id}, type={self.type})>'
	