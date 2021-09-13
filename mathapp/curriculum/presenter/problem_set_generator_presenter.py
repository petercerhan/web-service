from flask import (
    flash, redirect, url_for, render_template, abort, send_from_directory
)

import json

class ProblemSetGeneratorPresenter:

    def problem_set_generator_type_options(self, lesson_id):
        return render_template('problem_set_generators/problem_set_generator_type_options.html', lesson_id=lesson_id)

    def create_list_problem_set_generator_form(self):
        return render_template('problem_set_generators/create_list_problem_set_generator.html')

    def edit_list_problem_set_generator_redirect(self, problem_set_generator):
        return redirect(url_for('problem_set_generators.edit_list_problem_set_generator', problem_set_generator_id=problem_set_generator['id']))

    def edit_list_problem_set_generator_form(self, problem_set_generator):
        return render_template('problem_set_generators/edit_list_problem_set_generator.html',
                                problem_set_generator=problem_set_generator,
                                exercises_json=json.dumps(problem_set_generator['exercises']))

    def edit_problem_set_generator_form_redirect(self, problem_set_generator):
        type = problem_set_generator['type']
        if type == 'list_problem_set_generator':
            return self.edit_list_problem_set_generator_form_redirect(problem_set_generator_id=problem_set_generator['id'])

    def edit_list_problem_set_generator_form_redirect(self, problem_set_generator_id):
        return redirect(url_for('problem_set_generators.edit_list_problem_set_generator', problem_set_generator_id=problem_set_generator_id))

    def add_exercises_form(self, 
                           problem_set_generator,
                           lesson,
                           add_exercise_options):
        return render_template('problem_set_generators/add_exercises.html',
                               problem_set_generator=problem_set_generator,
                               lesson=lesson,
                               exercises_json=json.dumps(add_exercise_options))
