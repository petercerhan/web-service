from mathapp.curriculum.interactor.domain_to_data_transforms.exercise import exercise_to_data

def list_problem_set_dto_template_to_data(list_problem_set_dto_template):
	exercises_data = [exercise_to_data(x) for x in list_problem_set_dto_template.exercises]
	return {'type': list_problem_set_dto_template.type,
			'exercises': exercises_data}