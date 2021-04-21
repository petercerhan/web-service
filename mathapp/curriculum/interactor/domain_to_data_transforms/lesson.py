
def lesson_to_data(lesson):
	return {'id': lesson.get_id(),
			'name': lesson.get_name(),
			'position': lesson.get_position()}