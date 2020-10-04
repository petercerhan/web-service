from flask import (
    request, flash, redirect, url_for, render_template, abort
)
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError
import json

import sys

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
            course_id = self.request.args.get('course_id')
            return self._get_create_form(course_id=course_id)

    def _get_create_form(self, course_id, error=None):
        course = self._get_course_or_none(course_id)
        return self._lesson_presenter.present_create(error=error, course=course)

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

        add_to_course_id = self.request.form.get('add_to_course_id')

        try:
            self._lesson_interactor.create(fields=fields, add_to_course_id=add_to_course_id)
            return self._lesson_presenter.present_create_successful(add_to_course_id=add_to_course_id)
        except ValidationError as error:
            return self._get_create_form(course_id=add_to_course_id, error=error)

    def handle_update_request(self, lesson_id, course_id=None):
        if self.request.method == 'POST':
            return self._post_update_form(lesson_id)
        else:
            return self._get_update_form(lesson_id, course_id)

    def _post_update_form(self, id):
        fields = {}
        fields['name'] = self.request.form.get('name')
        fields['display_name'] = self.request.form.get('display_name')
        lesson_sections = self.request.form.get('lesson_sections')
        if lesson_sections is not None:
            fields['lesson_sections'] = json.loads( lesson_sections )

        return_to_course_id = self.request.form.get('return_to_course_id')

        try:
            self._lesson_interactor.update(id, fields)
            return self._lesson_presenter.present_update_successful(return_to_course_id)
        except NotFoundError as error:
            self._lesson_presenter.present_not_found(error)
        except ValidationError as error:
            return self._get_update_form(id=id, return_to_course_id=return_to_course_id, error=error)


    def _get_update_form(self, id, return_to_course_id, error=None):
        try:
            lesson = self._lesson_interactor.read(id)
            return self._lesson_presenter.present_update(lesson, return_to_course_id, error=error)
        except NotFoundError as error:
            self._lesson_presenter.present_not_found(error)


    def handle_delete_request(self, id):
        try:
            self._lesson_interactor.delete(id)
        except NotFoundError as error:
            self._lesson_presenter.present_not_found(error)

        return self._lesson_presenter.present_delete_successful()










