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