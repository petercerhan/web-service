

def list_problem_set_generator_to_data(list_problem_set_generator):
	return {'id': list_problem_set_generator.get_id(), 
			'type': list_problem_set_generator.get_type(), 
			'name': list_problem_set_generator.get_name()}

