from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.diagram_exercise import DiagramExercise
from mathapp.curriculum.data_mapper.exercise.orm_exercise import ORMExercise

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMDiagramExercise(ORMExercise):
    __tablename__ = 'diagram_exercise'
    id = Column(Integer, ForeignKey('exercise.id'), primary_key=True)
    text = Column(String)
    diagram_image_data = Column(LargeBinary)
    source_code_filename = Column(String)
    correct_option = Column(String)
    incorrect_option_1 = Column(String)
    incorrect_option_2 = Column(String)
    incorrect_option_3 = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'diagram_exercise'
    }

    def __init__(self,
                 name,
                 tag,
                 text,
                 diagram_image_data,
                 source_code_filename,
                 correct_option,
                 incorrect_option_1,
                 incorrect_option_2,
                 incorrect_option_3):
        self.text = text
        self.diagram_image_data = diagram_image_data
        self.source_code_filename = source_code_filename
        self.correct_option = correct_option
        self.incorrect_option_1 = incorrect_option_1
        self.incorrect_option_2 = incorrect_option_2
        self.incorrect_option_3 = incorrect_option_3
        super().__init__(name=name, tag=tag)
        self._diagram_exercise = None

    @orm.reconstructor
    def init_on_load(self):
        self._diagram_exercise = None
        super().init_on_load()


    def get_model(self, unit_of_work):
        if self._diagram_exercise is not None:
            return self._diagram_exercise

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        diagram_exercise = DiagramExercise(name=self.name,
                                           tag=self.tag,
                                           text=self.text,
                                           diagram_image_data=self.diagram_image_data,
                                           source_code_filename=self.source_code_filename,
                                           correct_option=self.correct_option,
                                           incorrect_option_1=self.incorrect_option_1,
                                           incorrect_option_2=self.incorrect_option_2,
                                           incorrect_option_3=self.incorrect_option_3,
                                           unit_of_work=domain_model_unit_of_work)
        diagram_exercise._id = self.id
        self._diagram_exercise = diagram_exercise
        super()._set_model(diagram_exercise)
        return diagram_exercise

    def sync_id(self):
        self._diagram_exercise._id = self.id

    def sync_fields(self):
        self.text = self._diagram_exercise._text
        self.diagram_image_data = self._diagram_exercise._diagram_image_data
        self.source_code_filename = self._diagram_exercise._source_code_filename
        self.correct_option = self._diagram_exercise._correct_option
        self.incorrect_option_1 = self._diagram_exercise._incorrect_option_1
        self.incorrect_option_2 = self._diagram_exercise._incorrect_option_2
        self.incorrect_option_3 = self._diagram_exercise._incorrect_option_3
        super().sync_fields()

    def __repr__(self):
        return f'<ORMDiagramExercise(id={self.id}, type={self.type})>'





