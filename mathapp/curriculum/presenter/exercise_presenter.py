from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class ExercisePresenter:

	def __init__(self, file_service):
		self._file_service = file_service

	def create_formula_exercise_form(self, topic):
		return render_template('exercises/create_formula_exercise.html', topic=topic)

	def create_diagram_exercise_form(self, topic):
		return render_template('exercises/create_diagram_exercise.html', topic=topic)

	def edit_formula_exercise_form(self, formula_exercise):
		return render_template('exercises/edit_formula_exercise.html', formula_exercise=formula_exercise)

	def edit_diagram_exercise_form(self, diagram_exercise):
		source_code_file_extension = self._file_service.get_extension_for_filename(diagram_exercise['source_code_filename'])
		return render_template('exercises/edit_diagram_exercise.html', 
							   diagram_exercise=diagram_exercise,
							   source_code_file_extension=source_code_file_extension)



