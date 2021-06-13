from sqlalchemy import Column, Integer, String, ForeignKey, Table
from mathapp.sqlalchemy.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from mathapp.curriculum.domain_model.list_problem_set_generator import ListProblemSetGenerator
from mathapp.curriculum.data_mapper.problem_set_generator.orm_problem_set_generator import ORMProblemSetGenerator

from mathapp.curriculum.data_mapper.exercise.exercise_list_value_holder import ExerciseListValueHolder
from mathapp.curriculum.data_mapper.lesson.lesson_value_holder import LessonValueHolder

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMListProblemSetGenerator(ORMProblemSetGenerator):
    __tablename__ = 'list_problem_set_generator'
    id = Column(Integer, ForeignKey('problem_set_generator.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'list_problem_set_generator'
    }

    def __init__(self, name):
        super().__init__(name=name)
        self._list_problem_set_generator = None

    @orm.reconstructor
    def init_on_load(self):
        self._list_problem_set_generator = None
        super().init_on_load()

    def get_model(self, unit_of_work):
        if self._list_problem_set_generator is not None:
            return self._list_problem_set_generator

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)
        exercise_list_value_holder = ExerciseListValueHolder(orm_model=self, unit_of_work=unit_of_work)
        lesson_value_holder = LessonValueHolder(orm_model=self, unit_of_work=unit_of_work)

        list_problem_set_generator = ListProblemSetGenerator(name=self.name,
                                                             exercise_list_value_holder=exercise_list_value_holder,
                                                             lesson_value_holder=lesson_value_holder,
                                                             unit_of_work=domain_model_unit_of_work)
        list_problem_set_generator._id = self.id
        self._list_problem_set_generator = list_problem_set_generator
        super()._set_model(list_problem_set_generator)
        return list_problem_set_generator

    def sync_id(self):
        self._list_problem_set_generator._id = self.id

    def sync_fields(self):
        super().sync_fields()




    def __repr__(self):
         return f'<ORMListProblemSetGenerator(id={self.id}, type={self.type})>'