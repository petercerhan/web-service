from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.libraries.data_mapper_library.base import Base

from mathapp.student.domain_model.exercise_event import ExerciseEvent

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMExerciseEvent(Base):
    __tablename__ = 'exercise_event'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    exercise_id = Column(Integer, ForeignKey('exercise.id'))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    completed = Column(Boolean)
    correct = Column(Boolean)
    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime)
    client_timezone = Column(String)
    activity_data = Column(String)

    def __init__(self,
                 student_id,
                 exercise_id,
                 lesson_id,
                 completed,
                 correct,
                 start_datetime,
                 end_datetime,
                 client_timezone,
                 activity_data):
        self.student_id = student_id
        self.exercise_id = exercise_id
        self.lesson_id = lesson_id
        self.completed = completed
        self.correct = correct
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.client_timezone = client_timezone
        self.activity_data = activity_data
        self._exercise_event = None

    @orm.reconstructor
    def init_on_load(self):
        self._exercise_event = None

    def get_model(self, unit_of_work):
        if self._exercise_event is not None:
            return self._exercise_event

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        exercise_event = ExerciseEvent(completed=self.completed,
                                       correct=self.correct,
                                       unit_of_work=domain_model_unit_of_work)
        exercise_event._id = self.id
        self._exercise_event = exercise_event
        return exercise_event

    def sync_id(self):
        self._exercise_event._id = self.id

    def sync_fields(self):
        self.completed = self._exercise_event._completed
        self.correct = self._exercise_event._correct


    def __repr__(self):
        return f'<ORMExerciseEvent ID(id={self.id})>'

















