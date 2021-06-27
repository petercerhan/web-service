from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.libraries.general_library.errors.mathapp_error import MathAppError

import json

class TopicWebController:

	def __init__(self,
				request,
				topic_interactor,
				topic_presenter,
				course_presenter):
		self._request = request
		self._topic_interactor = topic_interactor
		self._topic_presenter = topic_presenter
		self._course_presenter = course_presenter

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

	def get_edit_form(self, topic_id):
		try:
			topic = self._topic_interactor.get(topic_id)
			return self._topic_presenter.edit_form(topic=topic)
		except MathAppError as error:
			return error.message

	def post_edit_form(self, course_id, topic_id):
		fields = {}
		fields['display_name'] = self._request.form.get('display_name')

		lessons = self._request.form.get('lessons')
		if lessons is not None:
			fields['lessons'] = json.loads(lessons)

		try:
			self._topic_interactor.update(id=topic_id, fields=fields)
			return self._topic_presenter.edit_course_form(course_id=course_id)
		except MathAppError as error:
			return error.message


	def get_create_lesson_form(self, topic_id):
		return self._topic_presenter.create_lesson_form()

	def post_create_lesson_form(self, topic_id):
		fields = {}
		fields['name'] = self._request.form.get('name')

		try:
			self._topic_interactor.create_lesson(topic_id=topic_id, fields=fields)
			return self._topic_presenter.edit_form_redirect(topic_id=topic_id)
		except MathAppError as error:
			return error.message

	def delete_lesson(self, topic_id, lesson_id):
		try:
			topic = self._topic_interactor.delete_lesson(topic_id=topic_id, lesson_id=lesson_id)
			return self._topic_presenter.edit_form_redirect(topic_id=topic_id)
		except MathAppError as error:
			return error.message


	def delete(self, topic_id):
		try:
			self._topic_interactor.delete(topic_id)
			return self._course_presenter.index_redirect()
		except MathAppError as error:
			return error.message


	def get_edit_exercises_form(self, topic_id):
		try:
			topic = self._topic_interactor.get(topic_id)
			return self._topic_presenter.edit_exercises_form(topic=topic)
		except MathAppError as error:
			return error.message












