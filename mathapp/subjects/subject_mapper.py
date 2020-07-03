from mathapp.subjects.orm_subject import ORMSubject
from mathapp.subjects.subject import Subject
from mathapp.subjects.subject_unit_of_work_decorator import SubjectUnitOfWorkDecorator

class SubjectMapper:

    def __init__(self, orm_subject):
        self._orm_subject = orm_subject

        unit_of_work = SubjectUnitOfWorkDecorator(subject_mapper = self)

        subject = Subject(name=orm_subject.name, unit_of_work = unit_of_work)
        subject._id = orm_subject.id

        self._subject = subject

    def get_subject(self):
        return self._subject