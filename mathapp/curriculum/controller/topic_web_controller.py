from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.mathapp_error import MathAppError

import json

import sys

class TopicWebController:

	def __init__(self,
				request,
				topic_interactor,
				topic_presenter):
		self._request = request
		self._topic_interactor = topic_interactor
		self._topic_presenter = topic_presenter

	def get_index(self):
		topics = self._topic_interactor.list()
		return self._topic_presenter.index(topics)

	def get_create_form(self, course_id):
		return self._topic_presenter.create_form(course_id)

	def post_create_form(self, course_id):
		fields = {}
		fields['name'] = self._request.form.get('name')
		fields['display_name'] = self._request.form.get('display_name')

		try:
			topic = self._topic_interactor.create(fields=fields)
			return self._topic_presenter.create_course_topic_form(course_id, topic['id'])
		except ValidationError as error:
			return self._topic_presenter.create_form(course_id, error=error)

	def get_edit_form(self, course_id, topic_id):
		return self._edit_form(course_id=course_id, topic_id=topic_id)

	def post_edit_form(self, course_id, topic_id):
		fields = {}
		fields['display_name'] = self._request.form.get('display_name')

		try:
			self._topic_interactor.update(id=topic_id, fields=fields)
			return self._topic_presenter.edit_course_form(course_id=course_id)
		except MathAppError as error:
			return self._edit_form(course_id=course_id, topic_id=topic_id, error=error)

	def _edit_form(self, course_id, topic_id, error=None):
		try:
			topic = self._topic_interactor.get(topic_id)
			return self._topic_presenter.edit_form(course_id=course_id, topic=topic, error=error)
		except MathAppError as error:
			return error.message


	def get_create_lesson_form(self, course_id, topic_id):
		return self._topic_presenter.create_lesson_form()

	def post_create_lesson_form(self, course_id, topic_id):
		fields = {}
		fields['name'] = self._request.form.get('name')

		try:
			self._topic_interactor.create_lesson(topic_id=topic_id, fields=fields)
			return self._topic_presenter.edit_topic_form_redirect(course_id=course_id, topic_id=topic_id)
		except MathAppError as error:
			return self._topic_presenter.create_lesson_form(error=error)
















