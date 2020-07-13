from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.sqlalchemy.lesson.orm_lesson import ORMLesson
from mathapp.sqlalchemy.base import Base

from mathapp.sqlalchemy.subject.subject_unit_of_work_decorator import SubjectUnitOfWorkDecorator
from mathapp.domain.entities.subject import Subject


class ORMSubject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    lessons = relationship('ORMLesson')

    @orm.reconstructor
    def init_on_load(self):
    	self._subject = None

    def get_model(self, unit_of_work):
    	if self._subject is not None:
    		return self._subject

    	unit_of_work_decorator = SubjectUnitOfWorkDecorator(unit_of_work=unit_of_work, orm_subject=self)
    	
    	subject = Subject(name=self.name, unit_of_work=unit_of_work_decorator)
    	subject._id = self.id

    	self._subject = subject
    	return subject

    def sync_id(self):
    	self._subject.id = self.id

    def sync_fields(self):
    	self.name = self._subject._name

    def __repr__(self):
        return "<Subject(subject='%s') ID(id='%s')>" % (self.name, self.id)
