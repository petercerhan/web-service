

def lesson_section_to_data(lesson_section):
	return {'id': lesson_section.get_id(), 
			'position': lesson_section.get_position(), 
			'type': lesson_section.get_type()}