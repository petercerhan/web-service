
from __future__ import print_function # In python 2.7
import sys

from mathapp.db import get_db
from mathapp.validation_error import ValidationError

class SubjectService:

    def list(self):
        db = get_db()
        subjects = db.execute(
            'SELECT id, name'
            ' FROM subject'
        ).fetchall()
        return subjects


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
        return 'Subject placeholder'


        
