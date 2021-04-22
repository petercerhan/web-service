from mathapp.curriculum.interactor.domain_to_data_transforms.lesson_prior import lesson_to_data

def lesson_sequence_item_to_data(lesson_sequence_item):
	lesson_data = lesson_to_data(lesson_sequence_item.get_lesson())
	return {'id': lesson_sequence_item.get_id(), 
			'position': lesson_sequence_item.get_position(),
			'lesson': lesson_data}

