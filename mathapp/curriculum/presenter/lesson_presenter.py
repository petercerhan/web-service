from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class LessonPresenter:

	def present_index(self, lessons):
		return render_template('lessons/index.html', lessons = lessons, lessons_json = json.dumps(lessons))

	def present_create(self, course=None, error=None):
		if error is not None:
			flash(error.message)
		return render_template('lessons/create.html', course=course)

	def present_create_successful(self, add_to_course_id):
		if add_to_course_id is not None:
			return redirect(url_for('courses.update', id=add_to_course_id))
		else:
			return redirect(url_for('lessons.index'))

	def present_update(self, lesson, error):
		if error is not None:
			flash(error.message)

		return render_template('lessons/update.html', lesson=lesson)

	def present_update_successful(self):
		return redirect(url_for('lessons.index'))
		
	def present_delete_successful(self):
		return redirect(url_for('lessons.index'))

	def present_not_found(self, error):
		abort(404, error.message)
	