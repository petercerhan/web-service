from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.curriculum.domain_model.topic import Topic

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMTopic(Base):
    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    display_name = Column(String)

    def __init__(self,
                name,
                display_name):
        self.name = name
        self.display_name = display_name
        self._topic = None

    @orm.reconstructor
    def init_on_load(self):
        self._topic = None

    def get_model(self, unit_of_work):
        if self._topic is not None:
            return self._topic

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        topic = Topic(name=self.name,
                      display_name=self.display_name,
                      unit_of_work=domain_model_unit_of_work)
        topic._id = self.id

        self._topic = topic
        return topic

    def sync_id(self):
        self._topic.id = self.id

    def sync_fields(self):
        self.name = self._topic._name
        self.display_name = self._topic._display_name

    def __repr__(self):
        return "<ORMTopic(name='%s') ID(id='%s')>" % (self.name, self.id)


