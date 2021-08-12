from sqlalchemy import Column, Integer, String, ForeignKey
from mathapp.libraries.data_mapper_library.base import Base
from sqlalchemy import orm
from sqlalchemy.orm import relationship

from mathapp.libraries.data_mapper_library.domain_model_unit_of_work import DomainModelUnitOfWork

from mathapp.libraries.data_mapper_library.value_holder import ValueHolder

from mathapp.student.domain_model.student_course import StudentCourse

class ORMStudentCourse(Base):
    __tablename__ = 'student_course'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    configured_course_push_number = Column(Integer)

    course = relationship('ORMCourse', uselist=False)

    def __init__(self, 
                 course_id, 
                 configured_course_push_number):
        self.course_id = course_id
        self.configured_course_push_number = configured_course_push_number
        self._student_course = None

    @orm.reconstructor
    def init_on_load(self):
        self._student_course = None

    def get_model(self, unit_of_work):
        if self._student_course is not None:
            return self._student_course

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        course_value_holder = ValueHolder(orm_model=self,
                                          property_name='course',
                                          set_at_init=(self.course_id is not None),
                                          unit_of_work=unit_of_work)

        student_course = StudentCourse(configured_course_push_number=self.configured_course_push_number,
                                       course_value_holder=course_value_holder,
                                       unit_of_work=domain_model_unit_of_work)

        student_course._id = self.id

        self._student_course = student_course
        return student_course

    def sync_id(self):
        self._student_course._id = self.id

    def sync_fields(self):
        self.configured_course_push_number = self._student_course._configured_course_push_number

    def __repr__(self):
        return f'<ORMStudentCourse ID(id={self.id})>'



