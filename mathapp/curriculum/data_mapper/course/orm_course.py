import sys

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson
from mathapp.curriculum.data_mapper.lesson_sequence_item.orm_lesson_sequence_item import ORMLessonSequenceItem
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.data_mapper.course.course_unit_of_work_decorator import CourseUnitOfWorkDecorator
from mathapp.curriculum.domain_model.course import Course
from mathapp.curriculum.data_mapper.lesson_sequence_item.lesson_sequence_item_list_value_holder import LessonSequenceItemListValueHolder


class ORMCourse(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    lesson_sequence_items = relationship('ORMLessonSequenceItem')

    def __init__(self, name):
        self.name = name
        self._course = None

    @orm.reconstructor
    def init_on_load(self):
        self._course = None

    def get_model(self, unit_of_work):
        if self._course is not None:
            return self._course

        unit_of_work_decorator = CourseUnitOfWorkDecorator(unit_of_work=unit_of_work, orm_course=self)
        lesson_sequence_item_list_value_holder = LessonSequenceItemListValueHolder(orm_model=self, unit_of_work=unit_of_work)
        
        course = Course(name=self.name, 
                        lesson_sequence_item_list_value_holder=lesson_sequence_item_list_value_holder,
                        unit_of_work=unit_of_work_decorator)
        course._id = self.id

        self._course = course
        return course

    def sync_id(self):
        self._course.id = self.id

    def sync_fields(self):
        self.name = self._course._name

    def __repr__(self):
        return "<ORMCourse(name='%s') ID(id='%s')>" % (self.name, self.id)
