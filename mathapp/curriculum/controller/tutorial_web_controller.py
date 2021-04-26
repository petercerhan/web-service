from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.mathapp_error import MathAppError

import json

class TutorialWebController:

	def __init__(self,
				 request,
				 tutorial_presenter,
				 tutorial_interactor):
		self._request = request
		self._tutorial_presenter = tutorial_presenter
		self._tutorial_interactor = tutorial_interactor

	def get_create_form(self, course_id, lesson_id):
		return self._tutorial_presenter.create_form()

	def post_create_form(self, course_id, lesson_id):
		fields = {}
		fields['name'] = self._request.form.get('name')

		try: 
			self._tutorial_interactor.create(fields=fields, lesson_id=lesson_id)
			return self._tutorial_presenter.edit_lesson_form_redirect(course_id=course_id, lesson_id=lesson_id)
		except MathAppError as error:
			return self._tutorial_presenter.create_form(error=error)

	def get_edit_form(self, course_id, tutorial_id):
		try:
			tutorial = self._tutorial_interactor.get(tutorial_id)
			return self._tutorial_presenter.edit_form(course_id=course_id, tutorial=tutorial)
		except MathAppError as error:
			return error.message