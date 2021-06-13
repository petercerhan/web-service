from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.mathapp_error import MathAppError

import json

class ProblemSetGeneratorWebController:

    def __init__(self,
                 request,
                 problem_set_generator_interactor,
                 problem_set_generator_presenter):
        self._request = request
        self._problem_set_generator_interactor = problem_set_generator_interactor
        self._problem_set_generator_presenter = problem_set_generator_presenter

    def get_create_list_problem_set_generator_form(self, course_id, lesson_id):
        return self._problem_set_generator_presenter.create_list_problem_set_generator_form()

    def post_create_list_problem_set_generator_form(self, course_id, lesson_id):
        fields = {}
        fields['name'] = self._request.form.get('name')

        try:
            problem_set_generator = self._problem_set_generator_interactor.create_list_problem_set_generator(fields=fields, lesson_id=lesson_id)
            return self._problem_set_generator_presenter.edit_list_problem_set_generator_redirect(course_id=course_id, problem_set_generator=problem_set_generator)
        except MathAppError as error:
            return error.message

