from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class LessonPresenter:

	def present_index(self, lessons):
		return render_template('lessons/index.html', lessons = lessons, lessons_json = json.dumps(lessons))