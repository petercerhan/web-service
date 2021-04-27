from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data

import sys

def tutorial_to_data(tutorial):
	return {'id': tutorial.get_id(),
			'name': tutorial.get_name()}

def tutorial_to_enriched_data(tutorial):
	lesson = lesson_to_data(tutorial.get_lesson())
	tutorial_steps = tutorial.get_tutorial_steps()
	print(f'tutorial steps: {tutorial_steps}', file=sys.stderr)
	return {'id': tutorial.get_id(),
			'name': tutorial.get_name(),
			'lesson': lesson}