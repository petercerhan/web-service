from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data

def list_problem_set_generator_to_data(list_problem_set_generator):
	lesson = lesson_to_data(list_problem_set_generator.get_lesson())
	return {'id': list_problem_set_generator.get_id(), 
			'type': list_problem_set_generator.get_type(), 
			'name': list_problem_set_generator.get_name(),
			'lesson': lesson}

