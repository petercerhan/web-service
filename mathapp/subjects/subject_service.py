
from __future__ import print_function # In python 2.7
import sys

from mathapp.db import get_db
from mathapp.validation_error import ValidationError
from mathapp.not_found_error import NotFoundError

class SubjectService:

    def list(self):
        db = get_db()
        subjects = db.execute(
            'SELECT id, name'
            ' FROM subject'
        ).fetchall()
        return subjects
    
    
    def read(self, id):
        subject = self._get_subject(id)
        return subject


    def create(self, fields):
        name = fields.get('name')
        if not name:
            raise ValidationError(message = "Invalid fields")

        db = get_db()
        db.execute(
            'INSERT INTO subject (name)'
            ' VALUES (?)',
            (name,)
        )
        db.commit()
        
        return self._get_subject(id)


    def update(self, id, fields):
        subject = self._get_subject(id)
        name = fields.get('name')
        if not name:
            raise ValidationError(message = "Invalid fields")
            
        db = get_db()
        db.execute(
            'UPDATE subject SET name = ?'
            ' Where id = ?',
            (name, id)
        )
        db.commit()
            
        return self._get_subject(id)
            

    def _get_subject(self, id):
        subject = get_db().execute('SELECT id, name FROM subject WHERE id = ?', (id,)).fetchone()

        if subject is None:
            raise NotFoundError(message = "Subject id {0} doesn't exist.".format(id))

        return subject
        
    
    def delete(self, id):
        subject = self._get_subject(id)
        db = get_db()
        db.execute('DELETE FROM subject WHERE id = ?', (id,))
        db.commit()
        return subject
