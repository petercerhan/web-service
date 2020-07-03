from mathapp.subjects.orm_subject import ORMSubject
from mathapp.subjects.subject import Subject

class SubjectContainer:

    def __init__(self, orm_subject):
        self._orm_subject = orm_subject
        subject = Subject(name=orm_subject.name)
        subject._id = orm_subject.id
        self._subject = subject

    def get_subject(self):
        return self._subject