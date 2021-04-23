from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data

def lesson_to_enriched_data(lesson):
	topic = topic_to_data(lesson.get_topic())
	return {'id': lesson.get_id(),
			'name': lesson.get_name(),
			'position': lesson.get_position(),
			'topic': topic}