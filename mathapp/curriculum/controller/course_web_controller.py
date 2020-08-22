from flask import (
    request
)
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError
import json

import sys

class CourseWebController:
    
    def __init__(self, request, course_interactor, course_presenter):
        self.request = request
        self._course_interactor = course_interactor
        self._course_presenter = course_presenter
        
        
    def handle_index_request(self):
        courses = self._course_interactor.list()
        return self._course_presenter.present_index(courses)
        
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
            return self._course_presenter.present_create(error = error)
        else:
            return self._course_presenter.present_create_successful()

    def _get_create_form(self):
        return self._course_presenter.present_create(error = None)
        

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
            self._course_presenter.present_not_found(error)
        except ValidationError as error:
            return self._get_update_form(id, error)
            # return self._course_presenter.present_update(course, error)
        else:
            return self._course_presenter.present_update_successful()
            
    def _get_update_form(self, id, error = None):
        try:
            course = self._course_interactor.read(id)
            return self._course_presenter.present_update(course, error = error)
        except NotFoundError as error:
            self._course_presenter.present_not_found(error)
            

    def handle_delete_request(self, id):
        try:
            self._course_interactor.delete(id)
        except NotFoundError as error:
            self._course_presenter.present_not_found(error)
            
        return self._course_presenter.present_delete_successful()








