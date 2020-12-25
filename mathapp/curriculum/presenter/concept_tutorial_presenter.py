from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class ConceptTutorialPresenter:

	def __init__(self, request):
		self._request_path = request.path
		self._request_contains_error_arg = (request.args.get('error_message') is not None)


	def present_create(self, error=None):
		if error is not None:
			flash(error.message)
		return render_template('concept_tutorials/create.html')


	def present_update(self, lesson, concept_tutorial, error_message=None):
		target_path = url_for('concept_tutorials.update', lesson_id=lesson['id'], lesson_section_id=concept_tutorial['id'])

		if target_path != self._request_path:
			if error_message is not None:
				target_path = f'{target_path}?error_message={error_message}'
			return redirect(target_path)

		if self._request_contains_error_arg and error_message is None:
			return redirect(target_path)

		if error_message is not None:
			flash(error_message)

		return render_template('concept_tutorials/update.html', 
							   lesson=lesson, 
							   concept_tutorial=concept_tutorial, 
							   concept_tutorial_json=json.dumps(concept_tutorial))



	def present_create_successful(self, lesson_id):
		return redirect(url_for('lessons.update', id=lesson_id))
		

