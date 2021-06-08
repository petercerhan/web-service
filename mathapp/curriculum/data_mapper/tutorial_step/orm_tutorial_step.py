from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.tutorial_step import TutorialStep

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMTutorialStep(Base):
    __tablename__ = 'tutorial_step'
    id = Column(Integer, primary_key=True)
    tutorial_id = Column(Integer, ForeignKey('tutorial.id'))
    type = Column(String)
    position = Column(Integer)
    display_group = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'tutorial_step',
        'polymorphic_on': type
    }

    def __init__(self, position, display_group):
        self.position = position
        self.display_group = display_group
        self._tutorial_step = None

    @orm.reconstructor
    def init_on_load(self):
        self._tutorial_step = None

    def _set_model(self, model):
        self._tutorial_step = model

    def get_model(self, unit_of_work):
        if self._tutorial_step is not None:
            return self._tutorial_step

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        tutorial_step = TutorialStep(position=self.position,
                                     display_group=self.display_group,
                                     unit_of_work=domain_model_unit_of_work)
        tutorial_step._id = self.id
        self._tutorial_step = tutorial_step
        return tutorial_step

    def sync_id(self):
        self._tutorial_step._id = self.id

    def sync_fields(self):
        self.position = self._tutorial_step._position
        self.display_group = self._tutorial_step._display_group
        
    def __repr__(self):
         return f'<ORMTutorialStep(id={self.id}, type={self.type})>'

         