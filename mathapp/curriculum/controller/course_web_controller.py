from flask import (
    request
)
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError
from mathapp.libraries.general_library.errors.mathapp_error import MathAppError
import json

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
        fields['display_name'] = self.request.form.get('display_name')

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
        fields['display_name'] = self.request.form.get('display_name')

        course_topics = self.request.form.get('course_topics')
        if course_topics is not None:
            fields['course_topics'] = json.loads(course_topics)
        
        try:
            self._course_interactor.update(id, fields)
        except NotFoundError as error:
            self._course_presenter.present_not_found(error)
        except ValidationError as error:
            return self._get_update_form(id, error)
        else:
            return self._course_presenter.present_update_successful()
            
    def _get_update_form(self, id, error = None):
        try:
            course = self._course_interactor.read(id)
            return self._course_presenter.present_update(course, error=error)
        except NotFoundError as error:
            self._course_presenter.present_not_found(error)
            

    def handle_delete_request(self, id):
        try:
            self._course_interactor.delete(id)
        except NotFoundError as error:
            self._course_presenter.present_not_found(error)
            
        return self._course_presenter.present_delete_successful()



    def get_create_course_topic_form(self, course_id, topic_id):
        return self._course_presenter.create_course_topic_form(topic_id=topic_id)


    def post_create_course_topic_form(self, course_id):
        topic_id = self.request.form.get('topic_id')

        try:
            course = self._course_interactor.create_course_topic(course_id=course_id, topic_id=topic_id)
            return self._course_presenter.edit_course_redirect(course_id)
        except MathAppError as error:
            return self._course_presenter.create_course_topic_form(topic_id, error=error)


    def delete_course_topic(self, course_id, course_topic_id):
        try:
            course = self._course_interactor.delete_course_topic(course_id, course_topic_id)
            return self._course_presenter.edit_course_redirect(course_id)
        except MathAppError as error:
            return self._course_presenter.create_course_topic_form(topic_id, error=error)



