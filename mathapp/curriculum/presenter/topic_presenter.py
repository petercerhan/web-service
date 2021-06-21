from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class TopicPresenter:

	def index(self, topics):
		return render_template('topics/index.html', topics=topics)

	def create_form(self, course_id, error=None):
		if error is not None:
			flash(error.message)
		return render_template('topics/create.html')

	def create_course_topic_form(self, course_id, topic_id):
		target_path = url_for('courses.create_course_topic', course_id=course_id)
		target_path = f'{target_path}?topic_id={topic_id}'
		return redirect(target_path)
		
	def edit_form(self, topic):
		return render_template('topics/edit.html',
								topic=topic, 
								topic_json=json.dumps(topic))

	def edit_course_form(self, course_id):
		return redirect(url_for('courses.update', id=course_id))


	def create_lesson_form(self):
		return render_template('lessons/create.html')

	def edit_form_redirect(self, topic_id):
		target_path = url_for('topics.edit', topic_id=topic_id)
		return redirect(target_path)

	def edit_exercises_form(self, topic):
		return render_template('topics/edit_exercises.html',
							    topic=topic,
							    exercises_json=json.dumps(topic['exercises']))

	def edit_exercises_form_redirect(self, topic_id):
		return redirect(url_for('topics.edit_exercises', topic_id=topic_id))

