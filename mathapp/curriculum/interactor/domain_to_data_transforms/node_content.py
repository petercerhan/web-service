from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.lesson_intro import lesson_intro_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.detail_section import detail_section_to_data


def node_content_list_to_data(node_content_list):
	return [node_content_to_data(node_content) for node_content in node_content_list]

def node_content_to_data(node_content):
	if node_content.model_name == 'lesson':
		return {'model_name': node_content.model_name, 'model': lesson_to_data(node_content.model)}
	elif node_content.model_name == 'lesson_intro':
		return {'model_name': node_content.model_name, 'model': lesson_intro_to_data(node_content.model)}
	elif node_content.model_name == 'detail_section':
		return {'model_name': node_content.model_name, 'model': detail_section_to_data(node_content.model)}
