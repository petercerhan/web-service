from flask import (
    request, flash, redirect, url_for, render_template, abort
)
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError
import json

import sys

class CourseWebController:
    
    def __init__(self, request, course_interactor):
        self.request = request
        self._course_interactor = course_interactor
        
        
    def handle_index_request(self):
        courses = self._course_interactor.list()
        return render_template('courses/index.html', courses=courses)
        
        
    def handle_create_request(self):
        if self.request.method == 'POST':
            return self._post_create_form()
        else:
            return self._get_create_form()
    
    def _post_create_form(self):
        fields = {}
        fields['name'] = self.request.form.get('name')

        try:
            self._course_interactor.create(fields)
        except ValidationError as error:
            flash(error.message)
            return render_template('courses/create.html')
        else:
            return redirect(url_for('courses.index'))

    def _get_create_form(self):
        return render_template('courses/create.html')
        

    def handle_update_request(self, id):
        if self.request.method == 'POST':
            return self._post_update_form(id)
        else:
            return self._get_update_form(id)

    def _post_update_form(self, id):
        fields = {}
        fields['name'] = self.request.form.get('name')
        fields['lesson_sequence_items'] = json.loads( self.request.form.get('lesson_sequence_items') )
        
        try:
            self._course_interactor.update(id, fields)
        except NotFoundError as error:
            abort(404, error.message)
        except ValidationError as error:
            flash(error.message)
            return self._get_update_form(id)
        else:
            return redirect(url_for('courses.index'))
            
    def _get_update_form(self, id):
        try:
            course = self._course_interactor.read(id)
            return render_template('courses/update.html', course = course, course_json = json.dumps(course))
        except NotFoundError as error:
            abort(404, error.message)
            

    def handle_delete_request(self, id):
        try:
            self._course_interactor.delete(id)
        except NotFoundError as error:
            abort(404, error.message)
            
        return redirect(url_for('courses.index'))
