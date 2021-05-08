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

	def post_create_formula_step_form(self, course_id, tutorial_id):
		fields = {}
		fields['formula_latex'] = self._request.form.get('formula_latex')

		try:
			self._tutorial_step_interactor.create_formula_tutorial_step(tutorial_id=tutorial_id, fields=fields)
			return self._tutorial_step_presenter.edit_tutorial_form_redirect(course_id, tutorial_id)
		except MathAppError as error:
			return error.message

	def post_create_image_step_form(self, course_id, tutorial_id, user_id):
		source_code_file = self._request.files.get('source_code_file')
		image_file = self._request.files.get('image_file')
		fields = {}

		try:
			self._tutorial_step_interactor.create_image_tutorial_step(user_id=user_id,
																	  tutorial_id=tutorial_id,
																	  source_code_file=source_code_file,
																	  image_file=image_file,
																	  fields=fields)
			return self._tutorial_step_presenter.edit_tutorial_form_redirect(course_id, tutorial_id)
		except MathAppError as error:
			return error.message


	def get_edit_text_tutorial_step_form(self, course_id, tutorial_id, tutorial_step_id):
		try:
			text_tutorial_step = self._tutorial_step_interactor.read(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)
			return self._tutorial_step_presenter.edit_text_tutorial_step_form(tutorial_step=text_tutorial_step)
		except MathAppError as error:
			return error.message

	def post_edit_text_tutorial_step_form(self, course_id, tutorial_id, tutorial_step_id):
		fields = {}
		fields['text'] = self._request.form.get('text')
		fields['display_group'] = int(self._request.form.get('display_group'))

		try:
			self._tutorial_step_interactor.update_text_tutorial_step(tutorial_id=tutorial_id, 
												  					 tutorial_step_id=tutorial_step_id,
												  					 fields=fields)
			return self._tutorial_step_presenter.edit_tutorial_form_redirect(course_id, tutorial_id)
		except MathAppError as error:
			return error.message

	def get_edit_formula_tutorial_step_form(self, course_id, tutorial_id, tutorial_step_id):
		try:
			formula_tutorial_step = self._tutorial_step_interactor.read(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)
			return self._tutorial_step_presenter.edit_formula_tutorial_step_form(tutorial_step=formula_tutorial_step)
		except MathAppError as error:
			return error.message

	def post_edit_formula_tutorial_step_form(self, course_id, tutorial_id, tutorial_step_id):
		fields = {}
		fields['formula_latex'] = self._request.form.get('formula_latex')
		fields['display_group'] = int(self._request.form.get('display_group'))

		try:
			self._tutorial_step_interactor.update_formula_tutorial_step(tutorial_id=tutorial_id, 
												  					    tutorial_step_id=tutorial_step_id,
												  					    fields=fields)
			return self._tutorial_step_presenter.edit_tutorial_form_redirect(course_id, tutorial_id)
		except MathAppError as error:
			return error.message

	def delete(self, course_id, tutorial_id, tutorial_step_id):
		try: 
			self._tutorial_step_interactor.delete(tutorial_id=tutorial_id, tutorial_step_id=tutorial_step_id)
			return self._tutorial_step_presenter.edit_tutorial_form_redirect(course_id, tutorial_id)
		except MathAppError as error:
			return error.message
			





