from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from mathapp.auth import login_required
from mathapp.db import get_db

from mathapp.subjects.subjects_web_controller import SubjectsWebController

bp = Blueprint('subjects', __name__)

@bp.route('/')
def index():
    db = get_db()
    subjects = db.execute(
        'SELECT id, name'
        ' FROM subject'
    ).fetchall()
    return render_template('subjects/index.html', subjects=subjects)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    controller = SubjectsWebController()
    return controller.handleCreateRequest(request)


#    if request.method == 'POST':
#        name = request.form['name']
#        error = None
#
#        if not name:
#            error = 'Name is required.'
#
#        if error is not None:
#            flash(error)
#        else:
#            db = get_db()
#            db.execute(
#                'INSERT INTO subject (name)'
#                ' VALUES (?)',
#                (name,)
#            )
#            db.commit()
#            return redirect(url_for('subjects.index'))
#
#    return render_template('subjects/create.html')


def get_subject(id):
    subject = get_db().execute('SELECT id, name FROM subject WHERE id = ?', (id,)).fetchone()

    if subject is None:
        abort(404, "Subject id {0} doesn't exist.".format(id))

    return subject

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    subject = get_subject(id)

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
                'UPDATE subject SET name = ?'
                ' Where id = ?',
                (name, id)
            )
            db.commit()
            return redirect(url_for('subjects.index'))
    
    return render_template('subjects/update.html', subject=subject)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_subject(id)
    db = get_db()
    db.execute('DELETE FROM subject WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('subjects.index'))
