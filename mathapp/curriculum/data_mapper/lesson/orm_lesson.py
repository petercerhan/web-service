from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.curriculum.data_mapper.lesson_section.orm_lesson_section import ORMLessonSection
from mathapp.curriculum.data_mapper.lesson_intro.orm_lesson_intro import ORMLessonIntro
from mathapp.curriculum.data_mapper.concept_tutorial.orm_concept_tutorial import ORMConceptTutorial
from mathapp.curriculum.domain_model.lesson import Lesson

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.data_mapper.lesson_section.lesson_section_list_value_holder import LessonSectionListValueHolder

import sys

class ORMLesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    display_name = Column(String)

    lesson_sequence_items = relationship('ORMLessonSequenceItem', back_populates='lesson')

    lesson_sections = relationship('ORMLessonSection', 
                                    order_by='asc(ORMLessonSection.position)', 
                                    cascade='all, delete, delete-orphan')

    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name
        self._lesson = None

    @orm.reconstructor
    def init_on_load(self):
        self._lesson = None

    def get_model(self, unit_of_work):

        print(f'lesson has lesson_sequence_items: {self.lesson_sequence_items}', file=sys.stderr)

        if self._lesson is not None:
            return self._lesson

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
        lesson_section_list_value_holder = LessonSectionListValueHolder(orm_model=self, unit_of_work=unit_of_work)
        
        lesson = Lesson(name=self.name, 
                        display_name=self.display_name, 
                        lesson_section_list_value_holder=lesson_section_list_value_holder,
                        unit_of_work=domain_model_unit_of_work)
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