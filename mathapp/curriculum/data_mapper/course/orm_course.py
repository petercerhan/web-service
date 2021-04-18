from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import orm
from mathapp.sqlalchemy.base import Base

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.domain_model.course import Course

from mathapp.curriculum.data_mapper.course_topic.orm_course_topic import ORMCourseTopic
from mathapp.curriculum.data_mapper.lesson_sequence_item.orm_lesson_sequence_item import ORMLessonSequenceItem

from mathapp.curriculum.data_mapper.lesson_sequence_item.lesson_sequence_item_list_value_holder import LessonSequenceItemListValueHolder
from mathapp.curriculum.data_mapper.course_topic.course_topic_list_value_holder import CourseTopicListValueHolder

class ORMCourse(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    display_name = Column(String)

    lesson_sequence_items = relationship('ORMLessonSequenceItem', 
                                            order_by="asc(ORMLessonSequenceItem.position)", 
                                            cascade="all, delete, delete-orphan", 
                                            back_populates="course")

    course_topics = relationship('ORMCourseTopic',
                                 order_by='asc(ORMCourseTopic.position)',
                                 back_populates='course')

    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name
        self._course = None

    @orm.reconstructor
    def init_on_load(self):
        self._course = None

    def get_model(self, unit_of_work):
        if self._course is not None:
            return self._course

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
        lesson_sequence_item_list_value_holder = LessonSequenceItemListValueHolder(orm_model=self, unit_of_work=unit_of_work)
        course_topic_list_value_holder = CourseTopicListValueHolder(orm_model=self, unit_of_work=unit_of_work)
        
        course = Course(name=self.name, 
                        display_name=self.display_name,
                        lesson_sequence_item_list_value_holder=lesson_sequence_item_list_value_holder,
                        course_topic_list_value_holder=course_topic_list_value_holder,
                        unit_of_work=domain_model_unit_of_work)
        course._id = self.id

        self._course = course
        return course

    def sync_id(self):
        self._course.id = self.id

    def sync_fields(self):
        self.name = self._course._name
        self.display_name = self._course._display_name

    def __repr__(self):
        return "<ORMCourse(name='%s') ID(id='%s')>" % (self.name, self.id)
