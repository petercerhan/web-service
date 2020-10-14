from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class LessonIntroPresenter:

	def present_create(self, error=None):
		if error is not None:
			flash(error.message)
		return render_template('lesson_intros/create.html')

	def present_create_successful(self, lesson_id):
		return redirect(url_for('lessons.update', id=lesson_id))

	def present_update(self, lesson, lesson_intro, error=None):
		if error is not None:
			flash(error.message)

		return render_template('lesson_intros/update.html', 
								lesson=lesson, 
								lesson_intro=lesson_intro, 
								lesson_intro_json=json.dumps(lesson_intro))

	def present_update_successful(self, lesson_id):
		return redirect(url_for('lessons.update', id=lesson_id))

	def present_create_detail_section_successful(self, lesson_id, lesson_section_id):
		return redirect(url_for('lesson_intros.update', lesson_id=lesson_id, lesson_section_id=lesson_section_id))