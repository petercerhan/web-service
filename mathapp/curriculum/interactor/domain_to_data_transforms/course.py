from mathapp.curriculum.interactor.domain_to_data_transforms.lesson_sequence_item import lesson_sequence_item_to_data

def course_to_data(course):
	return {'id': course.get_id(), 
			'name': course.get_name(), 
			'display_name': course.get_display_name()}

def course_to_enriched_data(course):
	lesson_sequence_items_data = [lesson_sequence_item_to_data(lesson_sequence_item) for lesson_sequence_item in course.get_lesson_sequence_items()]
	return {'id': course.get_id(), 
			'name': course.get_name(), 
			'display_name': course.get_display_name(),
			'lesson_sequence_items': lesson_sequence_items_data}
