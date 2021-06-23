from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.domain_model.tutorial import Tutorial

from mathapp.curriculum.data_mapper.tutorial_step.orm_tutorial_step import ORMTutorialStep
from mathapp.curriculum.data_mapper.text_tutorial_step.orm_text_tutorial_step import ORMTextTutorialStep
from mathapp.curriculum.data_mapper.formula_tutorial_step.orm_formula_tutorial_step import ORMFormulaTutorialStep

from mathapp.libraries.data_mapper_library.value_holder import ValueHolder
from mathapp.curriculum.data_mapper.tutorial_step.tutorial_step_list_value_holder import TutorialStepListValueHolder

class ORMTutorial(Base):
    __tablename__ = 'tutorial'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    lesson = relationship('ORMLesson', 
                          uselist=False, 
                          lazy='joined',
                          back_populates='tutorial')
    tutorial_steps = relationship('ORMTutorialStep', order_by='asc(ORMTutorialStep.position)')

    def __init__(self,
                 name):
        self.name = name
        self._tutorial = None

    @orm.reconstructor
    def init_on_load(self):
        self._tutorial = None

    def get_model(self, unit_of_work):
        if self._tutorial is not None:
            return self._tutorial

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
        
        lesson_value_holder = ValueHolder(orm_model=self,
                                         property_name='lesson',
                                         set_at_init=(self.lesson is not None),
                                         unit_of_work=unit_of_work)

        
        tutorial_step_list_value_holder = TutorialStepListValueHolder(orm_model=self, unit_of_work=unit_of_work)
        tutorial = Tutorial(name=self.name,
                            lesson_value_holder=lesson_value_holder,
                            tutorial_step_list_value_holder=tutorial_step_list_value_holder,
                            unit_of_work=domain_model_unit_of_work)
        tutorial._id = self.id

        self._tutorial = tutorial
        return tutorial

    def sync_id(self):
        self._tutorial._id = self.id

    def sync_fields(self):
        self.name = self._tutorial._name

    def __repr__(self):
        return "<ORMTutorial(name='%s') ID(id='%s')>" % (self.name, self.id)



