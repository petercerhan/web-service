from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class TutorialStepPresenter:

	def edit_tutorial_form_redirect(self, course_id, tutorial_id):
		return redirect(url_for('tutorials.edit', course_id=course_id, tutorial_id=tutorial_id))