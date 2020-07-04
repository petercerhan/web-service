
from __future__ import print_function # In python 2.7
import sys

from mathapp.validation_error import ValidationError
from mathapp.not_found_error import NotFoundError

from mathapp.db_sqlalchemy import Session
from mathapp.subjects.orm_subject import ORMSubject


from sqlalchemy.orm import sessionmaker

class SubjectService:

    def __init__(self, subject_repository, subject_factory, unit_of_work_committer):
        self.subject_repository = subject_repository
        self.subject_factory = subject_factory
        self._unit_of_work_committer = unit_of_work_committer

    def list(self):
        values = self.subject_repository.list()
        return values
    
    
    def read(self, id):
        subject = self.subject_repository.get(id=id)
        return subject


    def create(self, fields):
        name = fields.get('name')
        if not name:
            raise ValidationError(message = "Invalid fields")
        
        subject = self.subject_factory.create(fields)

        self._unit_of_work_committer.commit()

        return subject


    def update(self, id, fields):
        subject = self.subject_repository.get(id=id)

        name = fields.get('name')
        if not name:
            raise ValidationError(message = "Invalid fields")

        subject.set_name(name)
        self._unit_of_work_committer.commit()

        return subject


    def _get_subject(self, id):
        subject = Session.query(ORMSubject).filter(Subject.id == id).first()

        if subject is None:
            raise NotFoundError(message = "Subject id {0} doesn't exist.".format(id))

        return subject
        
    
    def delete(self, id):
        subject = self.subject_repository.get(id=id)
        subject.delete()
        self._unit_of_work_committer.commit()
        return subject








