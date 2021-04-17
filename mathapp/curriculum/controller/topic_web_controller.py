from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.validation_error import ValidationError

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

