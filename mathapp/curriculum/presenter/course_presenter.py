from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class CoursePresenter:

	def present_index(self, courses):
		return render_template('courses/index.html', courses=courses)

	def present_create(self, error):
		if error is not None:
			flash(error.message)

		return render_template('courses/create.html')

	def present_create_successful(self):
		return redirect(url_for('courses.index'))

	def present_update(self, course, error):
		if error is not None:
			flash(error.message)

		return render_template('courses/update.html', 
								course=course, 
								course_json=json.dumps(course))
 
	def present_update_successful(self):
		return redirect(url_for('courses.index'))

	def present_delete_successful(self):
		return redirect(url_for('courses.index'))

	def present_delete_lesson_sequence_item_successful(self, course):
		return redirect(url_for('courses.update', id=course['id']))

	def present_not_found(self, error):
		abort(404, error.message)