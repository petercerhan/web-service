from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.libraries.general_library.errors.mathapp_error import MathAppError

import json

class LessonWebController:

	def __init__(self,
				request,
				lesson_interactor,
				lesson_presenter):
		self._request = request
		self._lesson_interactor = lesson_interactor
		self._lesson_presenter = lesson_presenter

	def get_edit_form(self, lesson_id):
		try:
			lesson = self._lesson_interactor.get(lesson_id)
			return self._lesson_presenter.edit_form(lesson=lesson)
		except MathAppError as error:
			return error.message
	
	def post_edit_form(self, lesson_id):
		fields = {}
		fields['name'] = self._request.form.get('name')

		try:
			self._lesson_interactor.update(id=lesson_id, fields=fields)
			return self._edit_form(course_id=course_id, lesson_id=lesson_id)
		except MathAppError as error:
			return error.message


