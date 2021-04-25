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

	def present_update(self, lesson, return_to_course_id, error):
		if error is not None:
			flash(error.message)

		return render_template('lessons/update.html', 
								lesson=lesson, 
								lesson_json=json.dumps(lesson),
								return_to_course_id=return_to_course_id)

	def present_update_successful(self, return_to_course_id):
		if return_to_course_id is not None:
			return redirect(url_for('courses.update', id=return_to_course_id))
		else:
			return redirect(url_for('lessons.index'))
		
	def present_delete_successful(self):
		return redirect(url_for('lessons.index'))

	def present_not_found(self, error):
		abort(404, error.message)
	
	def present_create_lesson_section(self, lesson_id):
		return render_template('lessons/create_lesson_section.html', lesson_id=lesson_id)

	def present_delete_lesson_section_successful(self, course_id, lesson_id):
		if course_id is not None:
			return redirect(url_for('lessons.updateForCourse', course_id=course_id, lesson_id=lesson_id))
		else:
			return redirect(url_for('lessons.update', id=lesson_id))