from mathapp.curriculum.interactor.domain_to_data_transforms.exercise import exercise_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data

def list_problem_set_generator_to_enriched_data(list_problem_set_generator):
	exercises = list_problem_set_generator.get_exercises()
	exercises_data = [exercise_to_data(x) for x in exercises]
	lesson = list_problem_set_generator.get_lesson()
	lesson_data = lesson_to_data(lesson)
	return {'id': list_problem_set_generator.get_id(), 
			'type': list_problem_set_generator.get_type(), 
			'name': list_problem_set_generator.get_name(),
			'exercises': exercises_data,
			'lesson': lesson_data}