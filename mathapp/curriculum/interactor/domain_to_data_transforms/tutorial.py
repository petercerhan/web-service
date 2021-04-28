from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial_step import tutorial_step_to_data

import sys

def tutorial_to_data(tutorial):
	return {'id': tutorial.get_id(),
			'name': tutorial.get_name()}

def tutorial_to_enriched_data(tutorial):
	lesson = lesson_to_data(tutorial.get_lesson())
	tutorial_steps = tutorial.get_tutorial_steps()
	tutorial_steps_data = [tutorial_step_to_data(x) for x in tutorial_steps]
	
	return {'id': tutorial.get_id(),
			'name': tutorial.get_name(),
			'lesson': lesson,
			'tutorial_steps': tutorial_steps_data}