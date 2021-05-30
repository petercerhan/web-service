

def formula_exercise_to_data(formula_exercise):
	return {'id': formula_exercise.get_id(), 
			'name': text_tutorial_step.get_name(), 
			'tag': text_tutorial_step.get_tag(),
			'text': text_tutorial_step.get_text(), 
			'formula_latex': text_tutorial_step.get_formula_latex(), 
			'correct_option': text_tutorial_step.get_correct_option(), 
			'incorrect_option_1': text_tutorial_step.get_incorrect_option_1(), 
			'incorrect_option_2': text_tutorial_step.get_incorrect_option_2(), 
			'incorrect_option_3': text_tutorial_step.get_incorrect_option_3()}