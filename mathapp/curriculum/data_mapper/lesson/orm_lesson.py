from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.curriculum.domain_model.lesson import Lesson

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork


from mathapp.libraries.data_mapper_library.value_holder import ValueHolder

from mathapp.curriculum.data_mapper.tutorial.tutorial_value_holder import TutorialValueHolder
from mathapp.curriculum.data_mapper.problem_set_generator.problem_set_generator_value_holder import ProblemSetGeneratorValueHolder

from mathapp.curriculum.data_mapper.tutorial.orm_tutorial import ORMTutorial
from mathapp.curriculum.data_mapper.problem_set_generator.orm_problem_set_generator import ORMProblemSetGenerator
from mathapp.curriculum.data_mapper.list_problem_set_generator.orm_list_problem_set_generator import ORMListProblemSetGenerator

class ORMLesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('topic.id'))
    name = Column(String)
    position = Column(Integer)
    tutorial_id = Column(Integer, ForeignKey('tutorial.id'))
    problem_set_generator_id = Column(Integer, ForeignKey('problem_set_generator.id'))

    topic = relationship('ORMTopic', back_populates='lessons')
    tutorial = relationship('ORMTutorial', back_populates='lesson')
    problem_set_generator = relationship('ORMProblemSetGenerator', back_populates='lesson')

    def __init__(self,
                 name,
                 position):
        self.name = name
        self.position = position
        self._lesson = None

    @orm.reconstructor
    def init_on_load(self):
        self._lesson = None

    def get_model(self, unit_of_work):
        if self._lesson is not None:
            return self._lesson

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
        topic_value_holder = ValueHolder(orm_model=self, 
                                         property_name='topic',
                                         set_at_init=(self.topic_id is not None),
                                         unit_of_work=unit_of_work)
        tutorial_value_holder = TutorialValueHolder(orm_model=self, unit_of_work=unit_of_work)
        problem_set_generator_value_holder = ProblemSetGeneratorValueHolder(orm_model=self, unit_of_work=unit_of_work)

        lesson = Lesson(name=self.name,
                        position=self.position,
                        topic_value_holder=topic_value_holder,
                        tutorial_value_holder=tutorial_value_holder,
                        problem_set_generator_value_holder=problem_set_generator_value_holder,
                        unit_of_work=domain_model_unit_of_work)
        lesson._id = self.id

        self._lesson = lesson
        return lesson

    def sync_id(self):
        self._lesson._id = self.id

    def sync_fields(self):
        self.name = self._lesson._name
        self.position = self._lesson._position

    def __repr__(self):
        return "<ORMLesson(name='%s') ID(id='%s')>" % (self.name, self.id)
