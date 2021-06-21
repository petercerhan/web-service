from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class LessonPresenter:

	def edit_form(self, lesson):
		return render_template('lessons/edit.html', lesson=lesson)