from flask import (
    request, flash, redirect, url_for, render_template, abort
)
from mathapp.domain.errors.validation_error import ValidationError
from mathapp.domain.errors.not_found_error import NotFoundError

class LessonWebController:

	def __init__(self, request, lesson_interactor):
		self.request = request
		self._lesson_interactor = lesson_interactor

	def handle_index_request(self):
		lessons = self._lesson_interactor.list()
		return render_template('lessons/index.html', lessons = lessons)