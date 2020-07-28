from flask import (
    request, flash, redirect, url_for, render_template, abort
)
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

class SubjectWebController:
    
    def __init__(self, request, subject_service):
        self.request = request
        self.subject_service = subject_service
        
        
    def handle_index_request(self):
        subjects = self.subject_service.list()
        return render_template('subjects/index.html', subjects=subjects)
        
        
    def handle_create_request(self):
        if self.request.method == 'POST':
            return self._post_create_form()
        else:
            return self._get_create_form()
    
    def _post_create_form(self):
        fields = {}
        fields['name'] = self.request.form.get('name')
        
        try:
            self.subject_service.create(fields)
        except ValidationError as error:
            flash(error.message)
            return render_template('subjects/create.html')
        else:
            return redirect(url_for('subjects.index'))

    def _get_create_form(self):
        return render_template('subjects/create.html')
        

    def handle_update_request(self, id):
        if self.request.method == 'POST':
            return self._post_update_form(id)
        else:
            return self._get_update_form(id)

    def _post_update_form(self, id):
        fields = {}
        fields['name'] = self.request.form.get('name')
        
        try:
            self.subject_service.update(id, fields)
        except NotFoundError as error:
            abort(404, error.message)
        except ValidationError as error:
            flash(error.message)
            return self._get_update_form(id)
        else:
            return redirect(url_for('subjects.index'))
            
    def _get_update_form(self, id):
        try:
            subject = self.subject_service.read(id)
            return render_template('subjects/update.html', subject = subject)
        except NotFoundError as error:
            abort(404, error.message)
            

    def handle_delete_request(self, id):
        try:
            self.subject_service.delete(id)
        except NotFoundError as error:
            abort(404, error.message)
            
        return redirect(url_for('subjects.index'))
