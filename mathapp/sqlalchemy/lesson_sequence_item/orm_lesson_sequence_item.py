from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy import orm

from mathapp.curriculum.data_mapper.lesson_sequence_item.lesson_sequence_item unit_of_work_decorator import LessonSequenceItemUnitOfWorkDecorator
from mathapp.curriculum.domain_model.lesson_sequence_item import LessonSequenceItem

class ORMLessonSequenceItem(Base):
	__tablename__ = 'lesson_sequence_item'
	id = Column(Integer, primary_key=True)
	position = Column(Integer)
	lesson_id = Column(Integer, ForeignKey('lesson.id'))
	course_id = Column(Integer, ForeignKey('course.id'))

	def __init__(self, position):
		self.position = position
		self._lesson_sequence_item = None

	@orm.reconstructor
	def init_on_load(self):
		self._lesson_sequence_item = None

	def get_model(self, unit_of_work):
		if self._lesson_sequence_item is not None:
			return self._lesson_sequence_item

		unit_of_work_decorator = LessonSequenceItemUnitOfWorkDecorator(unit_of_work=unit_of_work, orm_lesson_sequence_item=self)

		lesson_sequence_item = LessonSequenceItem(position=self.position, unit_of_work = unit_of_work_decorator)
		lesson_sequence_item._id = self.id

		self._lesson_sequence_item = lesson_sequence_item
		return lesson_sequence_item


	def __repr__(self):
		return "<ORM Lesson Sequence Item(position='%s') ID(id='%s')>" % (self.position, self.id)kk