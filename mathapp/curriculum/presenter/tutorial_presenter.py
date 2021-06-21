from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class TutorialPresenter:

	def create_form(self):
		return render_template('tutorials/create.html')

	def edit_form(self, tutorial):
		return render_template('tutorials/edit.html',
								tutorial=tutorial,
								tutorial_json=json.dumps(tutorial))

	def edit_lesson_form_redirect(self, lesson_id):
		return redirect(url_for('lessons.edit', lesson_id=lesson_id))


