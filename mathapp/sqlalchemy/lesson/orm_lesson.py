from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base


class ORMLesson(Base):
	__tablename__ = 'lesson'
	id = Column(Integer, primary_key=True)
	subject_id = Column(Integer, ForeignKey('subject.id'))
	name = Column(String)

	def __repr__(self):
		return "<Subject(subject='%s') ID(id='%s')>" % (self.name, self.id)