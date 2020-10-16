from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.lesson_section import LessonSection

from mathapp.curriculum.data_mapper.lesson_section.lesson_section_parent_value_holder import LessonSectionParentValueHolder

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMLessonSection(Base):
    __tablename__ = 'lesson_section'
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    type = Column(String)
    position = Column(Integer)
    complete_lesson = Column(Boolean)

    lesson = relationship('ORMLesson', back_populates='lesson_sections')

    __mapper_args__ = {
        'polymorphic_identity': 'lesson_section',
        'polymorphic_on': type
    }

    def __init__(self, position, complete_lesson):
        self.position = position
        self.complete_lesson = complete_lesson
        self._lesson_section = None

    @orm.reconstructor
    def init_on_load(self):
        self._lesson_section = None

    def _set_model(self, model):
        self._lesson_section = model

    def get_model(self, unit_of_work):
        if self._lesson_section is not None:
            return self._lesson_section

        parent_value_holder = LessonSectionParentValueHolder(orm_lesson_section=self, unit_of_work=unit_of_work)
        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        lesson_section = LessonSection(position=self.position,
                                       complete_lesson=self.complete_lesson, 
                                       parent_value_holder=parent_value_holder,
                                       unit_of_work=domain_model_unit_of_work)
        lesson_section._id = self.id

        self._lesson_section = lesson_section
        return lesson_section

    def sync_id(self):
        self._lesson_section._id = self.id

    def sync_fields(self):
        self.position = self._lesson_section._position
        self.complete_lesson = self._lesson_section._complete_lesson

    def __repr__(self):
        return f'<ORMLessonSection(id={self.id}, type={self.type})>'








