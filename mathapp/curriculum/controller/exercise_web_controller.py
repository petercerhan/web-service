from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.mathapp_error import MathAppError

class ExerciseWebController:

	def __init__(self,
				 request,
				 exercise_presenter,
				 topic_interactor):
		self._request = request
		self._exercise_presenter = exercise_presenter
		self._topic_interactor = topic_interactor

	def get_create_formula_exercise_form(self, course_id, topic_id):
		try:			
			topic = self._topic_interactor.get(topic_id)
			return  self._exercise_presenter.create_formula_exercise_form(topic=topic)
		except MathAppError as error:
			return error.message

