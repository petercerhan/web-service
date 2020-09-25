from mathapp.curriculum.interactor.domain_to_data_transforms.lesson_intro import lesson_intro_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.concept_tutorial import concept_tutorial_to_data

def lesson_section_to_data(lesson_section):
	type = lesson_section.get_type()
	if type == 'lesson_section':
		return _lesson_section_to_data(lesson_section)
	elif type == 'lesson_intro':
		return lesson_intro_to_data(lesson_section)
	elif type == 'concept_tutorial':
		return concept_tutorial_to_data(lesson_section)


def _lesson_section_to_data(lesson_section):
	return {'id': lesson_section.get_id(), 
			'position': lesson_section.get_position(),
			'display_name': f'Lesson Section {lesson_section.get_id()}',
			'type': lesson_section.get_type()}