from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.derivation_instruction_section import DerivationInstructionSection
from mathapp.curriculum.data_mapper.instruction_section.orm_instruction_section import ORMInstructionSection

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMDerivationInstructionSection(ORMInstructionSection):
	__tablename__ = 'derivation_instruction_section'
	id = Column(Integer, ForeignKey('instruction_section.id'), primary_key=True)
	display_name = Column(String)

	__mapper_args__ = {
		'polymorphic_identity': 'derivation_instruction_section'
	}

	def __init__(self, position, display_name):
		self.display_name = display_name
		super().__init__(position)
		self._derivation_instruction_section = None

	@orm.reconstructor
	def init_on_load(self):
		self._derivation_instruction_section = None
		super().init_on_load()

	def get_model(self, unit_of_work):
		if self._derivation_instruction_section is not None:
			return self._derivation_instruction_section

		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

		derivation_instruction_section = DerivationInstructionSection(position=self.position, 
																	  display_name=self.display_name, 
																	  unit_of_work=domain_model_unit_of_work)
		derivation_instruction_section._id = self.id

		self._derivation_instruction_section = derivation_instruction_section
		super()._set_model(derivation_instruction_section)
		return derivation_instruction_section

	def sync_id(self):
		self._derivation_instruction_section._id = self.id

	def sync_fields(self):
		self.display_name = self._derivation_instruction_section._display_name
		super().sync_fields()

	def __repr__(self):
		return f'<ORMDerivationInstructionSection(id={self.id}, display_name={self.display_name})>'


