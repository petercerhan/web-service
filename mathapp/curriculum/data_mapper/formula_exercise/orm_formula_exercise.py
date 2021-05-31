from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.formula_exercise import FormulaExercise
from mathapp.curriculum.data_mapper.exercise.orm_exercise import ORMExercise

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMFormulaExercise(ORMExercise):
    __tablename__ = 'formula_exercise'
    id = Column(Integer, ForeignKey('exercise.id'), primary_key=True)
    text = Column(String)
    formula_latex = Column(String)
    correct_option = Column(String)
    incorrect_option_1 = Column(String)
    incorrect_option_2 = Column(String)
    incorrect_option_3 = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'formula_exercise'
    }

    def __init__(self,
                 name,
                 tag,
                 text,
                 formula_latex,
                 correct_option,
                 incorrect_option_1,
                 incorrect_option_2,
                 incorrect_option_3):
        self.text = text
        self.formula_latex = formula_latex
        self.correct_option = correct_option
        self.incorrect_option_1 = incorrect_option_1
        self.incorrect_option_2 = incorrect_option_2
        self.incorrect_option_3 = incorrect_option_3
        super().__init__(name=name, tag=tag)
        self._formula_exercise = None

    @orm.reconstructor
    def init_on_load(self):
        self._formula_exercise = None
        super().init_on_load()

    def get_model(self, unit_of_work):
        if self._formula_exercise is not None:
            return self._formula_exercise

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        formula_exercise = FormulaExercise(name=self.name,
                                           tag=self.tag,
                                           text=self.text,
                                           formula_latex=self.formula_latex,
                                           correct_option=self.correct_option,
                                           incorrect_option_1=self.incorrect_option_1,
                                           incorrect_option_2=self.incorrect_option_2,
                                           incorrect_option_3=self.incorrect_option_3,
                                           unit_of_work=domain_model_unit_of_work)
        formula_exercise._id = self.id
        self._formula_exercise = formula_exercise
        super()._set_model(formula_exercise)
        return formula_exercise

    def sync_id(self):
        self._formula_exercise._id = self.id

    def sync_fields(self):
        self.text = text
        self.formula_latex = formula_latex
        self.correct_option = correct_option
        self.incorrect_option_1 = incorrect_option_1
        self.incorrect_option_2 = incorrect_option_2
        self.incorrect_option_3 = incorrect_option_3
        super().sync_fields()

    def __repr__(self):
        return f'<ORMFormulaExercise(id={self.id}, type={self.type})>'




