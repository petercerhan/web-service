from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.libraries.data_mapper_library.base import Base
from sqlalchemy import orm
from sqlalchemy.orm import relationship

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.student.domain_model.course_push_control import CoursePushControl

class ORMCoursePushControl(Base):
    __tablename__ = 'course_push_control'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'))
    current_course_push_number = Column(Integer)

    def __init__(self,
                 course_id,
                 current_course_push_number):
        self.course_id = course_id
        self.current_course_push_number = current_course_push_number
        self._course_push_control = None

    @orm.reconstructor
    def init_on_load(self):
        self._course_push_control = None

    def get_model(self, unit_of_work):
        if self._course_push_control is not None:
            return self._course_push_control

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        course_push_control = CoursePushControl(current_course_push_number=self.current_course_push_number,
                                                course_id=self.course_id,
                                                unit_of_work=domain_model_unit_of_work)
        course_push_control._id = self.id
        self._course_push_control = course_push_control
        return course_push_control

    def sync_id(self):
        self._course_push_control._id = self.id

    def sync_fields(self):
        self.current_course_push_number = self._course_push_control.current_course_push_number


    def __repr__(self):
        return f'<ORMCoursePushControl(id={self.id} course_id={self.course_id})>'


