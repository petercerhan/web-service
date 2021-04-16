from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy import orm
from sqlalchemy.orm import relationship

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.domain_model.course_topic import CourseTopic
from mathapp.curriculum.data_mapper.course.course_value_holder import CourseValueHolder
from mathapp.curriculum.data_mapper.topic.topic_value_holder import TopicValueHolder

class ORMCourseTopic(Base):
    __tablename__ = 'course_topic'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'))
    topic_id = Column(Integer, ForeignKey('topic.id'))
    position = Column(Integer)

    course = relationship('ORMCourse', back_populates='course_topics')
    topic = relationship('ORMTopic', lazy='joined')

    def __init__(self, position):
        self.position = position
        self._course_topic = None

    @orm.reconstructor
    def init_on_load(self):
        self._course_topic = None

    def get_model(self, unit_of_work):
        if self._course_topic is not None:
            return self._course_topic

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
        course_value_holder = CourseValueHolder(orm_model=self, unit_of_work=unit_of_work)
        topic_value_holder = TopicValueHolder(orm_model=self, unit_of_work=unit_of_work)

        course_topic = CourseTopic(position=self.position,
                                   course_value_holder=course_value_holder,
                                   topic_value_holder=topic_value_holder,
                                   unit_of_work=domain_model_unit_of_work)
        course_topic._id = self.id

        self._course_topic = course_topic
        return course_topic

    def sync_id(self):
        self._course_topic.id = self.id

    def sync_fields(self):
        self.position = self._course_topic._position

    def __repr__(self):
        return "<ORMCourseTopic(position='%s') ID(id='%s')>" % (self.position, self.id)
