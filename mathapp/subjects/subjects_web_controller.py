from flask import (
    request, flash, redirect, url_for, render_template
)
from mathapp.db import get_db

class SubjectsWebController:
    
    def __init__(self):
        pass
        
    def handleCreateRequest(self, request):
        if request.method == 'POST':
            name = request.form['name']
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

        return render_template('subjects/create.html')
    

