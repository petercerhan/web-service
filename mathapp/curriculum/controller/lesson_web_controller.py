from flask import (
    request, flash, redirect, url_for, render_template, abort
)
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError
import json

class LessonWebController:

    def __init__(self, 
                 request,
                 lesson_interactor, 
                 lesson_presenter, 
                 course_interactor):
        self.request = request
        self._lesson_interactor = lesson_interactor
        self._lesson_presenter = lesson_presenter
        self._course_interactor = course_interactor

    def handle_index_request(self):
        lessons = self._lesson_interactor.list()
        return self._lesson_presenter.present_index(lessons)

    def handle_create_request(self):
        if self.request.method == 'POST':
            return self._post_create_form()
        else:
            return self._get_create_form()

    def _get_create_form(self):
        course_id = self.request.args.get('course_id')
        course = self._get_course_or_none(course_id)
        return self._lesson_presenter.present_create(error=None, course=course)

    def _get_course_or_none(self, id):
        if id is None:
            return None

        try:
            course = self._course_interactor.read(id=id)
            return course
        except Exception:
            return None

    def _post_create_form(self):
        fields = {}
        fields['name'] = self.request.form.get('name')
        fields['display_name'] = self.request.form.get('display_name')

        try:
            self._lesson_interactor.create(fields)
        except ValidationError as error:
            return self._lesson_presenter.present_create(error = error)
        else:
            return self._lesson_presenter.present_create_successful()

    def handle_update_request(self, id):
        if self.request.method == 'POST':
            return self._post_update_form(id)
        else:
            return self._get_update_form(id)


    def _post_update_form(self, id):
        fields = {}
        fields['name'] = self.request.form.get('name')
        fields['display_name'] = self.request.form.get('display_name')

        try:
            self._lesson_interactor.update(id, fields)
            return self._lesson_presenter.present_update_successful()
        except NotFoundError as error:
            self._lesson_presenter.present_not_found(error)
        except ValidationError as error:
            return self._get_update_form(id=id, error=error)


    def _get_update_form(self, id, error=None):
        try:
            lesson = self._lesson_interactor.read(id)
            return self._lesson_presenter.present_update(lesson, error=error)
        except NotFoundError as error:
            self._lesson_presenter.present_not_found(error)


    def handle_delete_request(self, id):
        try:
            self._lesson_interactor.delete(id)
        except NotFoundError as error:
            self._lesson_presenter.present_not_found(error)

        return self._lesson_presenter.present_delete_successful()










