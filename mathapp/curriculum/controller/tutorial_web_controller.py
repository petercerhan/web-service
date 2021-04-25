from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.mathapp_error import MathAppError

import json

class TutorialWebController:

	def __init__(self,
				 request,
				 tutorial_presenter):
		self._request = request
		self._tutorial_presenter = tutorial_presenter

	def get_create_form(self, course_id, lesson_id):
		return self._tutorial_presenter.create_form()