from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.curriculum.data_mapper.lesson_section.orm_lesson_section import ORMLessonSection
from mathapp.curriculum.data_mapper.lesson.lesson_unit_of_work_decorator import LessonUnitOfWorkDecorator
from mathapp.curriculum.domain_model.lesson import Lesson


import sys

class ORMLesson(Base):
	__tablename__ = 'lesson'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	display_name = Column(String)

	lesson_sections = relationship('ORMLessonSection', order_by='asc(ORMLessonSection.position)')

	def __init__(self, name, display_name):
		self.name = name
		self.display_name = display_name
		self._lesson = None

	@orm.reconstructor
	def init_on_load(self):
		self._lesson = None

	def get_model(self, unit_of_work):

		print(f'lesson sections: {self.lesson_sections}', file=sys.stderr)

		if self._lesson is not None:
			return self._lesson

		unit_of_work_decorator = LessonUnitOfWorkDecorator(unit_of_work=unit_of_work, orm_lesson=self)
		
		lesson = Lesson(name=self.name, display_name=self.display_name, unit_of_work=unit_of_work_decorator)
		lesson._id = self.id

		self._lesson = lesson
		return lesson

	def sync_id(self):
		self._lesson.id = self.id

	def sync_fields(self):
		self.name = self._lesson._name
		self.display_name = self._lesson._display_name

	def __repr__(self):
		return "<ORMLesson(lesson='%s') ID(id='%s')>" % (self.name, self.id)