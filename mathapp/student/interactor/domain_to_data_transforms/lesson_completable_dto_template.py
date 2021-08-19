from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial import tutorial_to_enriched_data
from mathapp.curriculum.interactor.domain_to_data_transforms.problem_set_dto_template import problem_set_dto_template_to_data

def lesson_completable_dto_template_to_data(lesson_completable_dto_template):
	lesson_data = lesson_to_data(lesson_completable_dto_template.lesson)
	tutorial_data = _tutorial_to_data(lesson_completable_dto_template)
	problem_set = _problem_set_to_data(lesson_completable_dto_template)
	return {'lesson': lesson_data,
			'tutorial': tutorial_data,
			'problem_set': problem_set}

def _tutorial_to_data(lesson_completable_dto_template):
	if lesson_completable_dto_template.tutorial is not None:
		return tutorial_to_enriched_data(lesson_completable_dto_template.tutorial)
	return None

def _problem_set_to_data(lesson_completable_dto_template):
	if lesson_completable_dto_template.problem_set_dto_template is not None:
		return problem_set_dto_template_to_data(lesson_completable_dto_template.problem_set_dto_template)
	return None