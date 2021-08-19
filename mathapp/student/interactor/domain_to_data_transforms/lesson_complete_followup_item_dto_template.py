from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data

def lesson_complete_followup_item_dto_template_to_data(lesson_complete_followup_item_dto_template):
	lesson_data = lesson_to_data(lesson_complete_followup_item_dto_template.lesson)
	return {'lesson': lesson_data,
			'type': lesson_complete_followup_item_dto_template.type}



