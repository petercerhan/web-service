from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data

def topic_to_data(topic):
	return {'id': topic.get_id(),
			'name': topic.get_name(),
			'display_name': topic.get_display_name()}

def topic_to_enriched_data(topic):
	lessons = [lesson_to_data(lesson) for lesson in topic.get_lessons()]
	return {'id': topic.get_id(),
			'name': topic.get_name(),
			'display_name': topic.get_display_name(),
			'lessons': lessons}
