from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.libraries.data_mapper_library.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.curriculum.domain_model.topic import Topic

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMLesson

from mathapp.curriculum.data_mapper.exercise.orm_exercise import ORMExercise
from mathapp.curriculum.data_mapper.formula_exercise.orm_formula_exercise import ORMFormulaExercise

from mathapp.libraries.data_mapper_library.list_value_holder import ListValueHolder

class ORMTopic(Base):
    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    display_name = Column(String)

    lessons = relationship('ORMLesson', 
                           order_by='asc(ORMLesson.position)',
                           back_populates='topic')

    course_topics = relationship('ORMCourseTopic',
                                 back_populates='topic')

    exercises = relationship('ORMExercise',
                             back_populates='topic')

    def __init__(self,
                name,
                display_name):
        self.name = name
        self.display_name = display_name
        self._topic = None

    @orm.reconstructor
    def init_on_load(self):
        self._topic = None

    def get_model(self, unit_of_work):
        if self._topic is not None:
            return self._topic

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
        lesson_list_value_holder = ListValueHolder(orm_model=self, 
                                                         property_name='lessons', 
                                                         unit_of_work=unit_of_work)
        course_topic_list_value_holder = ListValueHolder(orm_model=self, 
                                                         property_name='course_topics', 
                                                         unit_of_work=unit_of_work)
        exercise_list_value_holder = ListValueHolder(orm_model=self, 
                                                         property_name='exercises', 
                                                         unit_of_work=unit_of_work)

        topic = Topic(name=self.name,
                      display_name=self.display_name,
                      lesson_list_value_holder=lesson_list_value_holder,
                      course_topic_list_value_holder=course_topic_list_value_holder,
                      exercise_list_value_holder=exercise_list_value_holder,
                      unit_of_work=domain_model_unit_of_work)
        topic._id = self.id

        self._topic = topic
        return topic

    def sync_id(self):
        self._topic._id = self.id

    def sync_fields(self):
        self.name = self._topic._name
        self.display_name = self._topic._display_name

    def __repr__(self):
        return "<ORMTopic(name='%s') ID(id='%s')>" % (self.name, self.id)


