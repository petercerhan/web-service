from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class LessonIntroPresenter:

	def present_create(self):
		return render_template('lesson_intros/create.html')