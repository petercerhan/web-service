from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from mathapp.libraries.data_mapper_library.base import Base
from sqlalchemy import orm
from sqlalchemy.orm import relationship

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.libraries.data_mapper_library.value_holder import ValueHolder
from mathapp.libraries.data_mapper_library.list_value_holder import ListValueHolder

from mathapp.student.domain_model.student_topic import StudentTopic

class ORMStudentTopic(Base):
    __tablename__ = 'student_topic'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    topic_id = Column(Integer, ForeignKey('topic.id'))
    lessons_completed = Column(Integer)
    total_lessons = Column(Integer)
    completed = Column(Boolean)

    topic = relationship('ORMTopic', uselist=False)

    lesson_events = relationship('ORMLessonEvent',
                                 secondary='join(ORMLesson, ORMLessonEvent, foreign(ORMLesson.id) == remote(ORMLessonEvent.lesson_id))',
                                 primaryjoin='foreign(ORMStudentTopic.topic_id) == remote(ORMLesson.topic_id)',
                                 secondaryjoin='foreign(ORMLessonEvent.lesson_id) == remote(ORMLesson.id)')

    def __init__(self,
                 student_id,
                 topic_id,
                 lessons_completed,
                 total_lessons,
                 completed):
        self.student_id = student_id
        self.topic_id = topic_id
        self.lessons_completed = lessons_completed
        self.total_lessons = total_lessons
        self.completed = completed
        self._student_topic = None

    @orm.reconstructor
    def init_on_load(self):
        self._student_topic = None

    def get_model(self, unit_of_work):
        if self._student_topic is not None:
            return self._student_topic

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        topic_value_holder = ValueHolder(orm_model=self,
                                          property_name='topic',
                                          set_at_init=(self.topic_id is not None),
                                          unit_of_work=unit_of_work)

        lesson_event_list_value_holder = ListValueHolder(orm_model=self,
                                                          property_name='lesson_events',
                                                          unit_of_work=unit_of_work)

        student_topic = StudentTopic(lessons_completed=self.lessons_completed,
                                     total_lessons=self.total_lessons,
                                     completed=self.completed,
                                     topic_value_holder=topic_value_holder,
                                     lesson_event_list_value_holder=lesson_event_list_value_holder,
                                     unit_of_work=domain_model_unit_of_work)
        student_topic._id = self.id

        self._student_topic = student_topic
        return student_topic

    def sync_id(self):
        self._student_topic._id = self.id

    def sync_fields(self):
        self.lessons_completed = self._student_topic._lessons_completed
        self.total_lessons = self._student_topic._total_lessons
        self.completed = self._student_topic._completed

    def __repr__(self):
        return f'<ORMStudentTopic ID(id={self.id})>'








        

