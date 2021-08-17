from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.libraries.data_mapper_library.base import Base

from mathapp.student.domain_model.lesson_event import LessonEvent

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMLessonEvent(Base):
    __tablename__ = 'lesson_event'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    completed = Column(Boolean)
    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime)
    client_timezone = Column(String)
    activity_data = Column(String)

    def __init__(self,
                 student_id,
                 lesson_id,
                 completed,
                 start_datetime,
                 end_datetime,
                 client_timezone,
                 activity_data):
        self.student_id = student_id
        self.lesson_id = lesson_id
        self.completed = completed
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.client_timezone = client_timezone
        self.activity_data = activity_data
        self._lesson_event = None

    @orm.reconstructor
    def init_on_load(self):
        self._lesson_event = None

    def get_model(self, unit_of_work):
        if self._lesson_event is not None:
            return self._lesson_event

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        lesson_event = LessonEvent(completed=self.completed,
                                   unit_of_work=domain_model_unit_of_work)
        lesson_event._id = self.id

        self._lesson_event = lesson_event
        return lesson_event

    def sync_id(self):
        self._lesson_event._id = self.id

    def sync_fields(self):
        self.completed = self._lesson_event._completed



    def __repr__(self):
        return f'<ORMLessonEvent ID(id={self.id})>'









