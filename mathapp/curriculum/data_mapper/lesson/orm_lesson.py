from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.curriculum.domain_model.lesson import Lesson

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMLesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('topic.id'))
    name = Column(String)
    position = Column(Integer)

    topic = relationship('ORMTopic', back_populates='lessons')

    def __init__(self,
                 name,
                 position):
        self.name = name
        self.position = position
        self._lesson = None

    @orm.reconstructor
    def init_on_load(self):
        self._lesson = None

    def get_model(self, unit_of_work):
        if self._lesson is not None:
            return self._lesson

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        lesson = Lesson(name=self.name,
                        position=self.position,
                        unit_of_work=domain_model_unit_of_work)
        lesson._id = self.id

        self._lesson = lesson
        return lesson

    def sync_id(self):
        self._lesson._id = self.id

    def sync_fields(self):
        self.name = self._lesson._name
        self.position = self._lesson._position

    def __repr__(self):
        return "<ORMLesson(name='%s') ID(id='%s')>" % (self.name, self.id)
