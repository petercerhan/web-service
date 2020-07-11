from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mathapp.sqlalchemy.lesson.orm_lesson import ORMLesson
from mathapp.sqlalchemy.base import Base

class ORMSubject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    lessons = relationship('ORMLesson')

    def __repr__(self):
        return "<Subject(subject='%s') ID(id='%s')>" % (self.name, self.id)
