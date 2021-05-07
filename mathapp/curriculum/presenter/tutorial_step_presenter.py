from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class TutorialStepPresenter:

	def edit_text_tutorial_step_form(self, tutorial_step, error=None):
		if error is not None:
			flash(error.message)
		return render_template('tutorial_steps/edit_text_tutorial_step.html', 
								tutorial_step=tutorial_step)

	def edit_formula_tutorial_step_form(self, tutorial_step):
		return render_template('tutorial_steps/edit_formula_tutorial_step.html', 
								tutorial_step=tutorial_step)

	def edit_tutorial_form_redirect(self, course_id, tutorial_id):
		return redirect(url_for('tutorials.edit', course_id=course_id, tutorial_id=tutorial_id))
