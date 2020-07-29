from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy import orm

from mathapp.curriculum.data_mapper.lesson.lesson_unit_of_work_decorator import LessonUnitOfWorkDecorator
from mathapp.curriculum.domain_model.lesson import Lesson

class ORMLesson(Base):
	__tablename__ = 'lesson'
	id = Column(Integer, primary_key=True)
	name = Column(String)

	def __init__(self, name):
		self.name = name
		self._lesson = None

	@orm.reconstructor
	def init_on_load(self):
		self._lesson = None

	def get_model(self, unit_of_work):
		if self._lesson is not None:
			return self._lesson

		unit_of_work_decorator = LessonUnitOfWorkDecorator(unit_of_work=unit_of_work, orm_lesson=self)
		
		lesson = Lesson(name=self.name, unit_of_work=unit_of_work_decorator)
		lesson._id = self.id

		self._lesson = lesson
		return lesson

	def __repr__(self):
		return "<Lesson(lesson='%s') ID(id='%s')>" % (self.name, self.id)