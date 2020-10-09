from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy import orm
from sqlalchemy.orm import relationship

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.domain_model.lesson_sequence_item import LessonSequenceItem
from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson
from mathapp.curriculum.data_mapper.course.course_value_holder import CourseValueHolder

class ORMLessonSequenceItem(Base):
    __tablename__ = 'lesson_sequence_item'
    id = Column(Integer, primary_key=True)
    position = Column(Integer)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    course_id = Column(Integer, ForeignKey('course.id'))

    lesson = relationship('ORMLesson', lazy='joined', back_populates='lesson_sequence_items')

    course = relationship('ORMCourse', back_populates='lesson_sequence_items')

    def __init__(self, position):
        self.position = position
        self._lesson_sequence_item = None

    @orm.reconstructor
    def init_on_load(self):
        self._lesson_sequence_item = None

    def get_model(self, unit_of_work):
        if self._lesson_sequence_item is not None:
            return self._lesson_sequence_item

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        course_value_holder = CourseValueHolder(orm_model=self, unit_of_work=unit_of_work)

        lesson_sequence_item = LessonSequenceItem(position=self.position,
                                                 lesson=self.lesson.get_model(unit_of_work=unit_of_work), 
                                                 course_value_holder=course_value_holder,
                                                 unit_of_work=domain_model_unit_of_work)
        lesson_sequence_item._id = self.id

        self._lesson_sequence_item = lesson_sequence_item
        return lesson_sequence_item

    def sync_id(self):
        self._lesson_sequence_item.id = self.id

    def sync_fields(self):
        self.position = self._lesson_sequence_item._position

    def __repr__(self):
        return "<ORM Lesson Sequence Item(position='%s') ID(id='%s')>" % (self.position, self.id)

