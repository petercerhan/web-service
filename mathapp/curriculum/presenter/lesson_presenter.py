from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class LessonPresenter:

	def edit_form(self, course_id, lesson, error=None):
		if error is not None:
			flash(error.message)
		return render_template('lessons/edit.html', course_id=course_id, lesson=lesson)