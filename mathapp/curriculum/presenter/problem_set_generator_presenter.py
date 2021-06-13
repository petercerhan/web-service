from flask import (
    flash, redirect, url_for, render_template, abort, send_from_directory
)

import json

class ProblemSetGeneratorPresenter:

    def create_list_problem_set_generator_form(self):
        return render_template('problem_set_generators/create_list_problem_set_generator.html')

    def edit_list_problem_set_generator_redirect(self, course_id, problem_set_generator):
        return 'edit_list_problem_set_generator_redirect'

    def edit_list_problem_set_generator_form(self, problem_set_generator):
        return render_template('problem_set_generators/edit_list_problem_set_generator.html',
                                problem_set_generator=problem_set_generator,
                                exercises_json=json.dumps(problem_set_generator['exercises']))

    def edit_list_problem_set_generator_form_redirect(self, course_id, problem_set_generator_id):
        return redirect(url_for('problem_set_generators.edit_list_problem_set_generator', course_id=course_id, problem_set_generator_id=problem_set_generator_id))


