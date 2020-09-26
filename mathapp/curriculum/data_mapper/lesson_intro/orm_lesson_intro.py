from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.lesson_intro import LessonIntro
from mathapp.curriculum.data_mapper.lesson_section.orm_lesson_section import ORMLessonSection

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMLessonIntro(ORMLessonSection):
    __tablename__ = 'lesson_intro'
    id = Column(Integer, ForeignKey('lesson_section.id'), primary_key=True)
    description = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'lesson_intro'
    }

    def __init__(self, position, complete_lesson, description):
        self.description = description

        super().__init__(position, complete_lesson)

        self._lesson_intro = None

    @orm.reconstructor
    def init_on_load(self):
        self._lesson_intro = None
        super().init_on_load()

    def get_model(self, unit_of_work):
        if self._lesson_intro is not None:
            return self._lesson_intro

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        lesson_intro = LessonIntro(position=self.position, 
                                    complete_lesson=self.complete_lesson, 
                                    description=self.description, 
                                    unit_of_work=domain_model_unit_of_work)
        lesson_intro._id = self.id

        self._lesson_intro = lesson_intro
        super()._set_model(lesson_intro)
        return lesson_intro

    def sync_id(self):
        self._lesson_intro._id = self.id

    def sync_fields(self):
        self.description = self._lesson_intro._description
        super().sync_fields()

    def __repr__(self):
        return f'<ORMLessonIntro(id={self.id}, type={self.type})>'