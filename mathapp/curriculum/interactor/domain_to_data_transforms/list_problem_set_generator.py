from mathapp.curriculum.interactor.domain_to_data_transforms.exercise import exercise_to_data

def list_problem_set_generator_to_data(list_problem_set_generator):
	return {'id': list_problem_set_generator.get_id(), 
			'type': list_problem_set_generator.get_type(), 
			'name': list_problem_set_generator.get_name()}

def list_problem_set_generator_to_enriched_data(list_problem_set_generator):
	exercises = list_problem_set_generator.get_exercises()
	exercises_data = [exercise_to_data(x) for x in exercises]
	return {'id': list_problem_set_generator.get_id(), 
			'type': list_problem_set_generator.get_type(), 
			'name': list_problem_set_generator.get_name(),
			'exercises': exercises_data}

