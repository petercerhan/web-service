from mathapp.curriculum.interactor.domain_to_data_transforms.list_problem_set_generator import list_problem_set_generator_to_data

def problem_set_generator_to_data(problem_set_generator):
	type = problem_set_generator.get_type()
	if type == 'list_problem_set_generator':
		return list_problem_set_generator_to_data(problem_set_generator)