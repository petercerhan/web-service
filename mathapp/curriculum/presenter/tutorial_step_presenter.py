from flask import (
    flash, redirect, url_for, render_template, abort, send_from_directory
)

import json

class TutorialStepPresenter:

	def __init__(self, file_service):
		self._file_service = file_service

	def edit_text_tutorial_step_form(self, tutorial_step, error=None):
		if error is not None:
			flash(error.message)
		return render_template('tutorial_steps/edit_text_tutorial_step.html', 
								tutorial_step=tutorial_step)

	def edit_formula_tutorial_step_form(self, tutorial_step):
		return render_template('tutorial_steps/edit_formula_tutorial_step.html', 
								tutorial_step=tutorial_step)

	def edit_image_tutorial_step_form(self, tutorial_id, tutorial_step):
		source_code_file_extension = self._file_service.get_extension_for_filename(tutorial_step['source_code_filename'])
		return render_template('tutorial_steps/edit_image_tutorial_step.html',
								tutorial_id=tutorial_id,
								tutorial_step=tutorial_step,
								source_code_file_extension=source_code_file_extension)

	def edit_tutorial_form_redirect(self, tutorial_id):
		return redirect(url_for('tutorials.edit', tutorial_id=tutorial_id))

	def file_download(self, filename):
		path = self._file_service.get_file_uploads_path()
		filename = self._file_service.secure_filename(filename)
		return send_from_directory(path, filename)


