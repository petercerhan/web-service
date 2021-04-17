from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class TopicPresenter:

	def index(self, topics):
		return render_template('topics/index.html', topics = topics)

	def create_form(self, course_id, error=None):
		if error is not None:
			flash(error.message)
		return render_template('topics/create.html')

	def create_course_topic_form(self, course_id, topic_id):
		target_path = url_for('courses.create_course_topic', course_id=course_id)
		target_path = f'{target_path}?topic_id={topic_id}'
		return redirect(target_path)
		

