from mathapp.student.interactor.domain_to_data_transforms.lesson_complete_followup_item_dto_template import lesson_complete_followup_item_dto_template_to_data

def lesson_followup_item_to_data(lesson_followup_item):
	type = lesson_followup_item.type
	if type == 'lesson_complete_followup_item':
		return lesson_complete_followup_item_dto_template_to_data(lesson_followup_item)