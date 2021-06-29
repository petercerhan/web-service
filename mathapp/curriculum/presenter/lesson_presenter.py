from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class LessonPresenter:

	def edit_form(self, lesson):
		edit_problem_set_generator_url = None
		if lesson['problem_set_generator'] is not None:
			edit_problem_set_generator_url = self._problem_set_generator_url(lesson['problem_set_generator'])
		return render_template('lessons/edit.html', 
								lesson=lesson,
								edit_problem_set_generator_url=edit_problem_set_generator_url)

	def _problem_set_generator_url(self, problem_set_generator):
		type = problem_set_generator['type']
		if type == 'list_problem_set_generator':
			return url_for('problem_set_generators.edit_list_problem_set_generator', problem_set_generator=problem_set_generator['id'])
