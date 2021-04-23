from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.mathapp_error import MathAppError

import json

class LessonWebController:

	def __init__(self,
				request,
				lesson_interactor):
		self._request = request
		self._lesson_interactor = lesson_interactor

	def get_edit_form(self, course_id, lesson_id):
		return self._lesson_interactor.get(lesson_id)
	