

def lesson_to_data(lesson):
	return {'id': lesson.get_id(), 
			'name': lesson.get_name(), 
			'display_name': lesson.get_display_name()}