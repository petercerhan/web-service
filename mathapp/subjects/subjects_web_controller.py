from flask import (
    request, flash, redirect, url_for, render_template, abort
)
from mathapp.db import get_db

class SubjectsWebController:
    
    def __init__(self, request):
        self.request = request
        
    def handle_index_request(self):
        db = get_db()
        subjects = db.execute(
            'SELECT id, name'
            ' FROM subject'
        ).fetchall()
        return render_template('subjects/index.html', subjects=subjects)
        
    def handle_create_request(self):
        if self.request.method == 'POST':
            return self._post_create_form()
        else:
            return render_template('subjects/create.html')
    
    def _post_create_form(self):
        name = self.request.form['name']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO subject (name)'
                ' VALUES (?)',
                (name,)
            )
            db.commit()
            return redirect(url_for('subjects.index'))

    def handle_update_request(self, id):
        if self.request.method == 'POST':
            return self._post_update_form(id)
        else:
            return render_template('subjects/update.html', subject=self._get_subject(id))

    def _post_update_form(self, id):
        subject = self._get_subject(id)
        name = self.request.form['name']
        error = None
        
        if not name:
            error = 'Name is required.'
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE subject SET name = ?'
                ' Where id = ?',
                (name, id)
            )
            db.commit()
            return redirect(url_for('subjects.index'))
    
        
    def _get_subject(self, id):
        subject = get_db().execute('SELECT id, name FROM subject WHERE id = ?', (id,)).fetchone()

        if subject is None:
            abort(404, "Subject id {0} doesn't exist.".format(id))

        return subject

    def handle_delete_request(self, id):
        self._get_subject(id)
        db = get_db()
        db.execute('DELETE FROM subject WHERE id = ?', (id,))
        db.commit()
        return redirect(url_for('subjects.index'))
