from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data

def course_topic_to_data(course_topic):
	topic_data = topic_to_data(course_topic.get_topic())
	return {'id': course_topic.get_id(),
			'position': course_topic.get_position(),
			'topic': topic_data}

