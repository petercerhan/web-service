from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.concept_tutorial import ConceptTutorial
from mathapp.curriculum.data_mapper.lesson_section.orm_lesson_section import ORMLessonSection
from mathapp.curriculum.data_mapper.concept_tutorial.concept_tutorial_unit_of_work_decorator import ConceptTutorialUnitOfWorkDecorator

class ORMConceptTutorial(ORMLessonSection):
	__tablename__ = 'concept_tutorial'
	id = Column(Integer, ForeignKey('lesson_section.id'), primary_key=True)
	display_name = Column(String)

	__mapper_args__ = {
		'polymorphic_identity': 'concept_tutorial'
	}

	def __init__(self, position, complete_lesson, display_name):
		self.display_name = display_name

		super().__init__(position, complete_lesson)

		self._concept_tutorial = None

	@orm.reconstructor
	def init_on_load(self):
		self._concept_tutorial = None

	def get_model(self, unit_of_work):
		if self._concept_tutorial is not None:
			return self._concept_tutorial

		unit_of_work_decorator = ConceptTutorialUnitOfWorkDecorator(unit_of_work=unit_of_work, orm_concept_tutorial=self)

		concept_tutorial = ConceptTutorial(position=self.position, 
											complete_lesson = self.complete_lesson, 
											display_name = self.display_name, 
											unit_of_work=unit_of_work_decorator)
		concept_tutorial._id = self.id

		self._concept_tutorial = concept_tutorial
		return concept_tutorial

	def sync_id(self):
		self._concept_tutorial._id = self.id

	def sync_fields(self):
		self.display_name = self._concept_tutorial._display_name
		super().sync_fields()

	def __repr__(self):
		return f'<ORMConceptTutorial(id={self.id}, type={self.type}>'