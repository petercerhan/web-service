from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

import sys

class ConceptTutorialPresenter:

	def __init__(self, request_path):
		self._request_path = request_path

	def present_create(self, error=None):
		if error is not None:
			flash(error.message)
		return render_template('concept_tutorials/create.html')

	def present_edit(self, lesson, concept_tutorial, error_message=None):
		target_path = url_for('concept_tutorials.update', lesson_id=lesson['id'], lesson_section_id=concept_tutorial['id'])
		if target_path != self._request_path:
			redirect(target_path)

		if error_message is not None:
			flash(error_message)

		return render_template('concept_tutorials/update.html', 
							   lesson=lesson, 
							   concept_tutorial=concept_tutorial, 
							   concept_tutorial_json=json.dumps(concept_tutorial))



	def present_create_successful(self, lesson_id):
		return redirect(url_for('lessons.update', id=lesson_id))
		

	def present_update_successful(self, lesson):
		return redirect(url_for('lessons.update', id=lesson['id']))


