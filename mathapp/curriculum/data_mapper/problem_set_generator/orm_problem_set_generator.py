from sqlalchemy import Column, Integer, String, ForeignKey, Table
from mathapp.libraries.data_mapper_library.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.curriculum.domain_model.problem_set_generator import ProblemSetGenerator

from mathapp.libraries.data_mapper_library.list_value_holder import ListValueHolder
from mathapp.libraries.data_mapper_library.value_holder import ValueHolder

association_table = Table('problem_set_generator_exercise_association', Base.metadata,
    Column('problem_set_generator_id', Integer, ForeignKey('problem_set_generator.id')),
    Column('exercise_id', Integer, ForeignKey('exercise.id'))
)

class ORMProblemSetGenerator(Base):
    __tablename__ = 'problem_set_generator'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String)

    lesson = relationship('ORMLesson', 
                           uselist=False, 
                           lazy='joined',
                           back_populates='problem_set_generator')
    exercises = relationship('ORMExercise',
                             secondary=association_table)

    __mapper_args__ = {
        'polymorphic_identity': 'problem_set_generator',
        'polymorphic_on': type
    }

    def __init__(self,
                 name):
        self.name = name
        self._problem_set_generator = None

    @orm.reconstructor
    def init_on_load(self):
        self._problem_set_generator = None

    def _set_model(self, model):
        self._problem_set_generator = model

    def get_model(self, unit_of_work):
        if self._problem_set_generator is not None:
            return self._problem_set_generator

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
        exercise_list_value_holder = ListValueHolder(orm_model=self, 
                                                         property_name='exercises', 
                                                         unit_of_work=unit_of_work)
        
        lesson_value_holder = ValueHolder(orm_model=self,
                                         property_name='lesson',
                                         set_at_init=(self.lesson is not None),
                                         unit_of_work=unit_of_work)

        problem_set_generator = ProblemSetGenerator(name=self.name,
                                                    exercise_list_value_holder=exercise_list_value_holder,
                                                    lesson_value_holder=lesson_value_holder,
                                                    unit_of_work=domain_model_unit_of_work)
        problem_set_generator._id = self.id

        self._problem_set_generator = problem_set_generator
        return problem_set_generator

    def sync_id(self):
        self._problem_set_generator._id = self.id

    def sync_fields(self):
        self.name = self._problem_set_generator._name



    def __repr__(self):
         return f'<ORMProblemSetGenerator(id={self.id}, type={self.type})>'


