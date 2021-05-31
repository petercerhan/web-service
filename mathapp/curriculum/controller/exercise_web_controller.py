from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.mathapp_error import MathAppError

class ExerciseWebController:

	def __init__(self,
				 request,
				 exercise_presenter,
				 exercise_interactor,
				 topic_presenter,
				 topic_interactor):
		self._request = request
		self._exercise_presenter = exercise_presenter
		self._exercise_interactor = exercise_interactor
		self._topic_presenter = topic_presenter
		self._topic_interactor = topic_interactor

	def get_create_formula_exercise_form(self, course_id, topic_id):
		try:			
			topic = self._topic_interactor.get(topic_id)
			return  self._exercise_presenter.create_formula_exercise_form(topic=topic)
		except MathAppError as error:
			return error.message

	def post_create_formula_exercise_form(self, course_id, topic_id):
		fields = {}
		fields['name'] = self._request.form.get('name')
		fields['tag'] = self._request.form.get('tag')
		fields['text'] = self._request.form.get('text')
		fields['formula_latex'] = self._request.form.get('formula_latex')
		fields['correct_option'] = self._request.form.get('correct_option')
		fields['incorrect_option_1'] = self._request.form.get('incorrect_option_1')
		fields['incorrect_option_2'] = self._request.form.get('incorrect_option_2')
		fields['incorrect_option_3'] = self._request.form.get('incorrect_option_3')
		try:
			self._exercise_interactor.create_formula_exercise(topic_id=topic_id, fields=fields)
			return self._topic_presenter.edit_exercises_form_redirect(course_id=course_id, topic_id=topic_id)
		except MathAppError as error:
			return error.message

	def get_create_diagram_exercise_form(self, course_id, topic_id):
		try:			
			topic = self._topic_interactor.get(topic_id)
			return  self._exercise_presenter.create_diagram_exercise_form(topic=topic)
		except MathAppError as error:
			return error.message








