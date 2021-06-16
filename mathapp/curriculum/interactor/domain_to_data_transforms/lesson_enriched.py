from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial import tutorial_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.problem_set_generator import problem_set_generator_to_data

def lesson_to_enriched_data(lesson):
	topic = topic_to_data(lesson.get_topic())
	
	tutorial = lesson.get_tutorial()
	tutorial_data = None
	if tutorial is not None:
		tutorial_data = tutorial_to_data(tutorial)

	problem_set_generator = lesson.get_problem_set_generator()
	problem_set_generator_data = None
	if problem_set_generator is not None:
		problem_set_generator_data = problem_set_generator_to_data(problem_set_generator)

	return {'id': lesson.get_id(),
			'name': lesson.get_name(),
			'position': lesson.get_position(),
			'topic': topic,
			'tutorial': tutorial_data,
			'problem_set_generator': problem_set_generator_data}