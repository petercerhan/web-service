

def lesson_intro_to_data(lesson_intro):
	return {'id': lesson_intro.get_id(), 
			'position': lesson_intro.get_position(), 
			'description': lesson_intro.get_description(), 
			'display_name': 'Lesson Intro',
			'type': lesson_intro.get_type()}