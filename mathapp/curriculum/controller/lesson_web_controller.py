from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.mathapp_error import MathAppError

import json

class LessonWebController:

	def __init__(self,
				request,
				lesson_interactor,
				lesson_presenter):
		self._request = request
		self._lesson_interactor = lesson_interactor
		self._lesson_presenter = lesson_presenter

	def get_edit_form(self, course_id, lesson_id):
		lesson = self._lesson_interactor.get(lesson_id)
		return self._lesson_presenter.edit_form(lesson)
	