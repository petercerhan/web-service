from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial import tutorial_to_enriched_data
from mathapp.curriculum.interactor.domain_to_data_transforms.problem_set_dto_template import problem_set_dto_template_to_data

def lesson_completable_dto_template_to_data(lesson_completable_dto_template):
	lesson_data = lesson_to_data(lesson_completable_dto_template.lesson)
	tutorial_data = tutorial_to_enriched_data(lesson_completable_dto_template.tutorial)
	problem_set = problem_set_dto_template_to_data(lesson_completable_dto_template.problem_set_dto_template)
	return {'lesson': lesson_data,
			'tutorial': tutorial_data,
			'problem_set': problem_set}