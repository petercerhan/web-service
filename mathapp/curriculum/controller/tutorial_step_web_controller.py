from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.mathapp_error import MathAppError

import json

class TutorialStepWebController:

	def __init__(self,
				 request,
				 tutorial_step_presenter,
				 tutorial_step_interactor):
		self._request = request
		self._tutorial_step_presenter = tutorial_step_presenter
		self._tutorial_step_interactor = tutorial_step_interactor

	def post_create_text_step_form(self, course_id, tutorial_id):
		fields = {}
		fields['text'] = self._request.form.get('text')

		try:
			self._tutorial_step_interactor.create_text_tutorial_step(tutorial_id=tutorial_id, fields=fields)
			return self._tutorial_step_presenter.edit_tutorial_form_redirect(course_id, tutorial_id)
		except MathAppError as error:
			return error.message