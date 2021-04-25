from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.domain_model.tutorial import Tutorial

class ORMTutorial(Base):
    __tablename__ = 'tutorial'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    lesson = relationship('ORMLesson', uselist=False, back_populates='tutorial')

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
        tutorial = Tutorial(name=self.name,
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



