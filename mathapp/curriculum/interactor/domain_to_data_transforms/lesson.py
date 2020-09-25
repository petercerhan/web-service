from mathapp.curriculum.interactor.domain_to_data_transforms.lesson_section import lesson_section_to_data

def lesson_to_data(lesson):
	return {'id': lesson.get_id(), 
			'name': lesson.get_name(), 
			'display_name': lesson.get_display_name()}

def lesson_to_enriched_data(lesson):
	lesson_sections = [lesson_section_to_data(lesson_section) for lesson_section in lesson.get_lesson_sections()]
	return {'id': lesson.get_id(), 
			'name': lesson.get_name(), 
			'display_name': lesson.get_display_name(), 
			'lesson_sections': lesson_sections}