from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class ConceptTutorialPresenter:

	def present_create(self, error=None):
		if error is not None:
			flash(error.message)
		return render_template('concept_tutorials/create.html')

	def present_create_successful(self, lesson_id):
		return redirect(url_for('lessons.update', id=lesson_id))

	def present_update(self, lesson, concept_tutorial, error=None):
		if error is not None:
			flash(error.message)

		return render_template('concept_tutorials/update.html', 
							   lesson=lesson, 
							   concept_tutorial=concept_tutorial, 
							   concept_tutorial_json=json.dumps(concept_tutorial))

	def present_update_successful(self, lesson):
		return redirect(url_for('lessons.update', id=lesson['id']))


