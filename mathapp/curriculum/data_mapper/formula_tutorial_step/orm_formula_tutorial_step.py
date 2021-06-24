from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.libraries.data_mapper_library.base import Base

from mathapp.curriculum.domain_model.formula_tutorial_step import FormulaTutorialStep
from mathapp.curriculum.data_mapper.tutorial_step.orm_tutorial_step import ORMTutorialStep

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMFormulaTutorialStep(ORMTutorialStep):
	__tablename__ = 'formula_tutorial_step'
	id = Column(Integer, ForeignKey('tutorial_step.id'), primary_key=True)
	formula_latex = Column(String)

	__mapper_args__ = {
		'polymorphic_identity': 'formula_tutorial_step'
	}

	def __init__(self,
				 position,
				 display_group,
				 formula_latex):
		self.formula_latex = formula_latex
		super().__init__(position=position, display_group=display_group)
		self._formula_tutorial_step = None

	@orm.reconstructor
	def init_on_load(self):
		self._formula_tutorial_step = None
		super().init_on_load()

	def get_model(self, unit_of_work):
		if self._formula_tutorial_step is not None:
			return self._formula_tutorial_step

		domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

		formula_tutorial_step = FormulaTutorialStep(position=self.position,
													display_group=self.display_group,
													formula_latex=self.formula_latex,
													unit_of_work=domain_model_unit_of_work)
		formula_tutorial_step._id = self.id
		self._formula_tutorial_step = formula_tutorial_step
		super()._set_model(formula_tutorial_step)
		return formula_tutorial_step

	def sync_id(self):
		self._formula_tutorial_step._id = self.id

	def sync_fields(self):
		self.formula_latex = self._formula_tutorial_step._formula_latex
		super().sync_fields()
	
	def __repr__(self):
		return f'<ORMFormulaTutorialStep(id={self.id}, type={self.type})>'