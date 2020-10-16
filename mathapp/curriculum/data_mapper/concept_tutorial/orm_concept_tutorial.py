from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.concept_tutorial import ConceptTutorial
from mathapp.curriculum.data_mapper.lesson_section.orm_lesson_section import ORMLessonSection
from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.data_mapper.lesson_section.lesson_section_parent_value_holder import LessonSectionParentValueHolder

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
        super().init_on_load()

    def get_model(self, unit_of_work):
        if self._concept_tutorial is not None:
            return self._concept_tutorial

        parent_value_holder = LessonSectionParentValueHolder(orm_lesson_section=self, unit_of_work=unit_of_work)
        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        concept_tutorial = ConceptTutorial(position=self.position, 
                                            complete_lesson = self.complete_lesson, 
                                            display_name = self.display_name, 
                                            parent_value_holder=parent_value_holder,
                                            unit_of_work=domain_model_unit_of_work)
        concept_tutorial._id = self.id

        self._concept_tutorial = concept_tutorial
        super()._set_model(concept_tutorial)
        return concept_tutorial

    def sync_id(self):
        self._concept_tutorial._id = self.id

    def sync_fields(self):
        self.display_name = self._concept_tutorial._display_name
        super().sync_fields()

    def __repr__(self):
        return f'<ORMConceptTutorial(id={self.id}, type={self.type}>'