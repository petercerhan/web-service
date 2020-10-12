from mathapp.curriculum.interactor.domain_to_data_transforms.instruction_section import instruction_section_to_data

def lesson_intro_to_data(lesson_intro):
	return {'id': lesson_intro.get_id(), 
			'position': lesson_intro.get_position(), 
			'description': lesson_intro.get_description(), 
			'display_name': 'Lesson Intro',
			'type': lesson_intro.get_type()}

def lesson_intro_to_enriched_data(lesson_intro):
	instruction_sections = [instruction_section_to_data(instruction_section) for instruction_section in lesson_intro.get_instruction_sections()]
	return {'id': lesson_intro.get_id(), 
			'position': lesson_intro.get_position(), 
			'description': lesson_intro.get_description(), 
			'display_name': 'Lesson Intro', 
			'instruction_sections': instruction_sections,
			'type': lesson_intro.get_type()}