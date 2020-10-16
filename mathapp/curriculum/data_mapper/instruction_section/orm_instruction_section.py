from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship

from mathapp.curriculum.data_mapper.instruction_section.instruction_section_parent_value_holder import InstructionSectionParentValueHolder
from mathapp.curriculum.domain_model.instruction_section import InstructionSection

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMInstructionSection(Base):
	__tablename__ = 'instruction_section'
	id = Column(Integer, primary_key=True)
	type = Column(String)
	position = Column(Integer)

	lesson_section_id = Column(Integer, ForeignKey('lesson_section.id'))

	lesson_intro = relationship('ORMLessonIntro', back_populates='instruction_sections')

	__mapper_args__ = {
		'polymorphic_identity': 'instruction_section',
		'polymorphic_on': type
	}

	def __init__(self, position):
		self.position = position
		self._instruction_section = None

	@orm.reconstructor
	def init_on_load(self):
		self._instruction_section = None

	def _set_model(self, model):
		self._instruction_section = model

	def get_model(self, unit_of_work):
		if self._instruction_section is not None:
			return self._instruction_section

		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
		parent_value_holder = InstructionSectionParentValueHolder(orm_instruction_section=self, unit_of_work=unit_of_work)

		instruction_section = InstructionSection(position=self.position, 
												 parent_value_holder=parent_value_holder,
												 unit_of_work=domain_model_unit_of_work)
		instruction_section._id = self.id

		self._instruction_section = instruction_section
		return instruction_section

	def sync_id(self):
		self._instruction_section._id = self.id

	def sync_fields(self):
		self.position = self._instruction_section._position

	def __repr__(self):
		return f'<ORMInstructionSection(id={self.id}, type={self.type})>'

