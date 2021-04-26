from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data

def tutorial_to_data(tutorial):
	return {'id': tutorial.get_id(),
			'name': tutorial.get_name()}

def tutorial_to_enriched_data(tutorial):
	lesson = lesson_to_data(tutorial.get_lesson())
	return {'id': tutorial.get_id(),
			'name': tutorial.get_name(),
			'lesson': lesson}