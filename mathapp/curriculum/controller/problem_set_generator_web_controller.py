from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.libraries.general_library.errors.mathapp_error import MathAppError

import json

class ProblemSetGeneratorWebController:

    def __init__(self,
                 request,
                 problem_set_generator_interactor,
                 problem_set_generator_presenter,
                 lesson_presenter):
        self._request = request
        self._problem_set_generator_interactor = problem_set_generator_interactor
        self._problem_set_generator_presenter = problem_set_generator_presenter
        self._lesson_presenter = lesson_presenter


    def get_create_problem_set_generator_type_options(self, lesson_id):
        return self._problem_set_generator_presenter.problem_set_generator_type_options(lesson_id)

    def get_create_list_problem_set_generator_form(self, lesson_id):
        return self._problem_set_generator_presenter.create_list_problem_set_generator_form()

    def post_create_list_problem_set_generator_form(self, lesson_id):
        fields = {}
        fields['name'] = self._request.form.get('name')

        try:
            problem_set_generator = self._problem_set_generator_interactor.create_list_problem_set_generator(fields=fields, lesson_id=lesson_id)
            return self._problem_set_generator_presenter.edit_list_problem_set_generator_redirect(problem_set_generator=problem_set_generator)
        except MathAppError as error:
            return error.message

    def get_edit_list_problem_set_generator_form(self, problem_set_generator_id):
        try:
            problem_set_generator = self._problem_set_generator_interactor.get_list_problem_set_generator(id=problem_set_generator_id)
            return self._problem_set_generator_presenter.edit_list_problem_set_generator_form(problem_set_generator=problem_set_generator)
        except MathAppError as error:
            return error.message

    def post_edit_list_problem_set_generator_form(self, problem_set_generator_id):
        fields = {}
        fields['name'] = self._request.form.get('name')

        try:
            self._problem_set_generator_interactor.update_list_problem_set_generator(id=problem_set_generator_id, fields=fields)
            return self._problem_set_generator_presenter.edit_list_problem_set_generator_form_redirect(problem_set_generator_id=problem_set_generator_id)
        except MathAppError as error:
            return error.message

    def get_add_exercises_form(self, problem_set_generator_id):
        try:
            problem_set_generator = self._problem_set_generator_interactor.get_list_problem_set_generator(id=problem_set_generator_id)
            add_exercise_options = self._problem_set_generator_interactor.get_add_exercise_options(problem_set_generator_id=problem_set_generator_id)
            return self._problem_set_generator_presenter.add_exercises_form(problem_set_generator=problem_set_generator,
                                                                            add_exercise_options=add_exercise_options)
        except MathAppError as error:
            return error.message

    def post_add_exercises_form(self, problem_set_generator_id):
        exercise_id_list = []
        for key, val in self._request.form.items():
            if val == 'on':
                exercise_id_list.append(key)

        try:
            problem_set_generator = self._problem_set_generator_interactor.add_exercises_to_generator(problem_set_generator_id=problem_set_generator_id, 
                                                                                                        exercise_id_list=exercise_id_list)
            return self._problem_set_generator_presenter.edit_problem_set_generator_form_redirect(problem_set_generator=problem_set_generator)
        except MathAppError as error:
            return error.message

    def remove_exercise_from_generator(self, problem_set_generator_id, exercise_id):
        try:
            problem_set_generator = self._problem_set_generator_interactor.remove_exercise_from_generator(problem_set_generator_id=problem_set_generator_id, 
                                                                                                          exercise_id=exercise_id)
            return self._problem_set_generator_presenter.edit_problem_set_generator_form_redirect(problem_set_generator=problem_set_generator)
        except MathAppError as error:
            return error.message


    def delete(self, id):
        try:
            problem_set_generator = self._problem_set_generator_interactor.get_problem_set_generator(id)
            self._problem_set_generator_interactor.delete(id=id)
            return self._lesson_presenter.edit_form_redirect(lesson_id=problem_set_generator['lesson']['id'])
        except MathAppError as error:
            return error.message









