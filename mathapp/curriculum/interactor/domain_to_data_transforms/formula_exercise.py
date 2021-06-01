

def formula_exercise_to_data(formula_exercise):
	return {'id': formula_exercise.get_id(), 
			'type': formula_exercise.get_type(), 
			'name': formula_exercise.get_name(), 
			'tag': formula_exercise.get_tag(),
			'text': formula_exercise.get_text(), 
			'formula_latex': formula_exercise.get_formula_latex(), 
			'correct_option': formula_exercise.get_correct_option(), 
			'incorrect_option_1': formula_exercise.get_incorrect_option_1(), 
			'incorrect_option_2': formula_exercise.get_incorrect_option_2(), 
			'incorrect_option_3': formula_exercise.get_incorrect_option_3()}