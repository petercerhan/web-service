

def formula_tutorial_step_to_data(formula_tutorial_step):
	return {'id': formula_tutorial_step.get_id(), 
			'position': formula_tutorial_step.get_position(), 
			'display_group': formula_tutorial_step.get_display_group(),
			'formula_latex': formula_tutorial_step.get_formula_latex(), 
			'type': formula_tutorial_step.get_type()}