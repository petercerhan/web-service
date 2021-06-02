from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class ExercisePresenter:

	def create_formula_exercise_form(self, topic):
		return render_template('exercises/create_formula_exercise.html', topic=topic)

	def create_diagram_exercise_form(self, topic):
		return render_template('exercises/create_diagram_exercise.html', topic=topic)

	def edit_formula_exercise_form(self, formula_exercise):
		return render_template('exercises/edit_formula_exercise.html', formula_exercise=formula_exercise)



