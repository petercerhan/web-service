from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String
from mathapp.subjects.clean_subject import CleanSubject

Base = declarative_base()

class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Subject(subject='%s') ID(id='%s')>" % (self.name, self.id)
