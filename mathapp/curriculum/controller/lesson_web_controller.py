from flask import (
    request, flash, redirect, url_for, render_template, abort
)
from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError
import json

class LessonWebController:

    def __init__(self, request, lesson_interactor, lesson_presenter):
        self.request = request
        self._lesson_interactor = lesson_interactor
        self._lesson_presenter = lesson_presenter

    def handle_index_request(self):
        lessons = self._lesson_interactor.list()
        return self._lesson_presenter.present_index(lessons)

    def handle_create_request(self):
        if self.request.method == 'POST':
            return self._post_create_form()
        else:
            return self._get_create_form()

    def _get_create_form(self):
        return self._lesson_presenter.present_create(error=None)

    def _post_create_form(self):
        fields = {}
        fields['name'] = self.request.form.get('name')

        try:
            self._lesson_interactor.create(fields)
        except ValidationError as error:
            return self._lesson_presenter.present_create(error = error)
        else:
            return self._lesson_presenter.present_create_successful()

        