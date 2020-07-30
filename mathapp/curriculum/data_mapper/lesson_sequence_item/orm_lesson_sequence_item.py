from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy import orm


class ORMLessonSequenceItem(Base):
	__tablename__ = 'lesson_sequence_item'
	id = Column(Integer, primary_key=True)
	position = Column(Integer)
	lesson_id = Column(Integer, ForeignKey('lesson.id'))
	course_id = Column(Integer, ForeignKey('course.id'))

	def __repr__(self):
		return "<ORM Lesson Sequence Item(position='%s') ID(id='%s')>" % (self.position, self.id)