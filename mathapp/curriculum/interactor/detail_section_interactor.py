from mathapp.curriculum.interactor.domain_to_data_transforms.detail_section import (detail_section_to_data, detail_section_to_enriched_data)
from mathapp.curriculum.interactor.domain_to_data_transforms.node_content import node_content_list_to_data
from mathapp.curriculum.domain_model.node_content import NodeContent
from mathapp.library.class_implements_method import class_implements_method

class DetailSectionInteractor:

	def __init__(self, detail_section_repository, unit_of_work):
		self._detail_section_repository = detail_section_repository
		self._unit_of_work = unit_of_work

	def read(self, id):
		detail_section = self._detail_section_repository.get(id)
		return detail_section_to_enriched_data(detail_section)

	def update(self, id, fields):
		detail_section = self._detail_section_repository.get(id)

		title = fields.get('title')
		if title is not None:
			detail_section.set_title(title)

		self._unit_of_work.commit()
		return detail_section_to_enriched_data(detail_section)

	def get_branch_for_node(self, id):
		detail_section = self._detail_section_repository.get(id)
		detail_section_node = NodeContent(model=detail_section, model_name='detail_section')
		nodes = [detail_section_node]
		node = detail_section_node
		while class_implements_method(node.model, 'get_parent'):
			node = node.model.get_parent()
			nodes.insert(0, node)

		return node_content_list_to_data(nodes)
