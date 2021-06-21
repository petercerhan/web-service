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

	def get_create_form(self, lesson_id):
		return self._tutorial_presenter.create_form()

	def post_create_form(self, lesson_id):
		fields = {}
		fields['name'] = self._request.form.get('name')

		try: 
			self._tutorial_interactor.create(fields=fields, lesson_id=lesson_id)
			return self._tutorial_presenter.edit_lesson_form_redirect(lesson_id=lesson_id)
		except MathAppError as error:
			error.message

	def get_edit_form(self, tutorial_id):
		try:
			tutorial = self._tutorial_interactor.get(tutorial_id)
			return self._tutorial_presenter.edit_form(tutorial=tutorial)
		except MathAppError as error:
			return error.message

	def post_edit_form(self, tutorial_id):
		fields = {}
		fields['name'] = self._request.form.get('name')

		tutorial_steps = self._request.form.get('tutorial_steps')
		if tutorial_steps is not None:
			fields['tutorial_steps'] = json.loads(tutorial_steps)

		try: 
			tutorial = self._tutorial_interactor.update(id=tutorial_id, fields=fields)
			return self._tutorial_presenter.edit_form(tutorial=tutorial)
		except MathAppError as error:
			error.message			

	def delete(self, tutorial_id):
		try:
			tutorial = self._tutorial_interactor.get(tutorial_id)
			self._tutorial_interactor.delete(tutorial_id)
			return self._tutorial_presenter.edit_lesson_form_redirect(lesson_id=tutorial['lesson']['id'])
		except MathAppError as error:
			return error.message



