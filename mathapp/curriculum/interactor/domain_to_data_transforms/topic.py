
def topic_to_data(topic):
	return {'id': topic.get_id(),
			'name': topic.get_name(),
			'display_name': topic.get_display_name()}