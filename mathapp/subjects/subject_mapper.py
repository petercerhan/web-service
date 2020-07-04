from mathapp.subjects.orm_subject import ORMSubject
from mathapp.subjects.subject import Subject
from mathapp.subjects.subject_unit_of_work_decorator import SubjectUnitOfWorkDecorator

class SubjectMapper:

    def __init__(self, unit_of_work, orm_subject):
        self._orm_subject = orm_subject

        unit_of_work = SubjectUnitOfWorkDecorator(unit_of_work = unit_of_work, subject_mapper = self)

        subject = Subject(name=orm_subject.name, unit_of_work = unit_of_work)
        subject._id = orm_subject.id

        self._subject = subject


    def get_model(self):
        return self._subject


    def get_orm_model(self):
    	return self._orm_subject


    def sync_id(self):
        self._subject._id = self._orm_subject.id


    def sync_orm_model(self):
        self._orm_subject.name = self._subject._name