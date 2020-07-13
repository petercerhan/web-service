import sys


from mathapp.domain.errors.validation_error import ValidationError
from mathapp.domain.errors.not_found_error import NotFoundError

class SubjectService:

    def __init__(self, subject_repository, subject_factory, unit_of_work_committer):
        self._subject_repository = subject_repository
        self._subject_factory = subject_factory
        self._unit_of_work_committer = unit_of_work_committer

    def list(self):
        values = self._subject_repository.list()
        return values
    
    
    def read(self, id):
        subject = self._subject_repository.get(id=id)
        subject2 = self._subject_repository.get(id=id)

        print(subject, file=sys.stderr)
        print(subject2, file=sys.stderr)

        subject.set_name("new_name")

        print(subject, file=sys.stderr)
        print(subject2, file=sys.stderr)



        return subject


    def create(self, fields):
        subject = self._subject_factory.create(fields)
        self._unit_of_work_committer.commit()
        return subject


    def update(self, id, fields):
        subject = self._subject_repository.get(id=id)

        name = fields.get('name')
        if name is not None:
            subject.set_name(name)

        self._unit_of_work_committer.commit()

        return subject
        
    
    def delete(self, id):
        subject = self._subject_repository.get(id=id)
        subject.delete()
        self._unit_of_work_committer.commit()
        return subject








