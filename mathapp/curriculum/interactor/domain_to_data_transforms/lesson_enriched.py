from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial import tutorial_to_data

def lesson_to_enriched_data(lesson):
	topic = topic_to_data(lesson.get_topic())
	tutorial = lesson.get_tutorial()
	tutorial_data = None
	if tutorial is not None:
		tutorial_data = tutorial_to_data(tutorial)
	return {'id': lesson.get_id(),
			'name': lesson.get_name(),
			'position': lesson.get_position(),
			'topic': topic,
			'tutorial': tutorial_data}