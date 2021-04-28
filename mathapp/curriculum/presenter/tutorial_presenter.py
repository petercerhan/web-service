from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class TutorialPresenter:

	def create_form(self, error=None):
		if error is not None:
			flash(error.message)
		return render_template('tutorials/create.html')

	def edit_form(self, course_id, tutorial, error=None):
		if error is not None:
			flash(error.message)
		return render_template('tutorials/edit.html', 
								course_id=course_id, 
								tutorial=tutorial,
								tutorial_json=json.dumps(tutorial))


	def edit_lesson_form_redirect(self, course_id, lesson_id):
		return redirect(url_for('lessons.edit', course_id=course_id, lesson_id=lesson_id))


