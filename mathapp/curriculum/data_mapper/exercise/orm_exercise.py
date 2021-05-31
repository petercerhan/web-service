from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.exercise import Exercise

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMExercise(Base):
    __tablename__ = 'exercise'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('topic.id'))
    type = Column(String)
    name = Column(String)
    tag = Column(String)

    topic = relationship('ORMTopic', uselist=False, lazy='joined', back_populates='exercises')

    __mapper_args__ = {
        'polymorphic_identity': 'exercise',
        'polymorphic_on': type
    }

    def __init__(self,
                 name,
                 tag):
        self.name = name
        self.tag = tag
        self._exercise = None

    @orm.reconstructor
    def init_on_load(self):
        self._exercise = None

    def _set_model(self, model):
        self._exercise = model

    def get_model(self, unit_of_work):
        if self._exercise is not None:
            return self._exercise

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        exercise = Exercise(name=self.name,
                            tag=self.tag,
                            unit_of_work=domain_model_unit_of_work)
        exercise._id = self.id
        self._exercise = exercise
        return exercise

    def sync_id(self):
        self._exercise._id = self.id

    def sync_fields(self):
        self.name = self._exercise.name
        self.tag = self._exercise.tag

    def __repr__(self):
         return f'<ORMExercise(id={self.id}, type={self.type})>'








