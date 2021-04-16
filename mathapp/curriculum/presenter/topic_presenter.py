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


