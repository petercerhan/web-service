from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.libraries.data_mapper_library.base import Base

from mathapp.student.domain_model.student import Student
from mathapp.system.data_mapper.role.orm_role import ORMRole

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMStudent(ORMRole):
     __tablename__ = 'student'
     id = Column(Integer, ForeignKey('role.id'), primary_key=True)

     __mapper_args__ = {
          'polymorphic_identity': 'student'
     }

     def __init__(self,
                  user_id):
          super().__init__(user_id=user_id)
          self._student = None

     @orm.reconstructor
     def init_on_load(self):
          self._student = None
          super().init_on_load()

     def get_model(self, unit_of_work):
          if self._student is not None:
               return self._student

          domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

          student = Student(unit_of_work=domain_model_unit_of_work)
          student._id = self.id
          self._student = student
          super()._set_model(student)
          return student

     def sync_id(self):
          self._student._id = self.id

     def sync_fields(self):
          super().sync_fields()
        
     def __repr__(self):
          return f'<Student(id={self.id}, type={self.type})>'







