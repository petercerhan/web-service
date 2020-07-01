
from __future__ import print_function # In python 2.7
import sys

from mathapp.validation_error import ValidationError
from mathapp.not_found_error import NotFoundError

from mathapp.db_sqlalchemy import Session
from mathapp.subjects.subject import Subject


from sqlalchemy.orm import sessionmaker

class SubjectService:

    def list(self):
        values = Session.query(Subject).all()
        return values
    
    
    def read(self, id):
        subject = self._get_subject(id)
        return subject


    def create(self, fields):
        name = fields.get('name')
        if not name:
            raise ValidationError(message = "Invalid fields")
            
        subject = Subject(name=name)
        Session.add(subject)
        Session.commit()
        return subject


    def update(self, id, fields):
        subject = self._get_subject(id)
        name = fields.get('name')
        if not name:
            raise ValidationError(message = "Invalid fields")

        subject.name = name
        Session.commit()
        return subject


    def _get_subject(self, id):
        subject = Session.query(Subject).filter(Subject.id == id).first()

        if subject is None:
            raise NotFoundError(message = "Subject id {0} doesn't exist.".format(id))

        return subject
        
    
    def delete(self, id):
        subject = self._get_subject(id)
        Session.delete(subject)
        Session.commit()
        return subject
