from mathapp.curriculum.interactor.domain_to_data_transforms.detail_section import detail_section_to_data
from mathapp.curriculum.domain_model.node_content import NodeContent

import sys

class DetailSectionInteractor:

	def __init__(self, detail_section_repository, unit_of_work):
		self._detail_section_repository = detail_section_repository
		self._unit_of_work = unit_of_work

	def read(self, id):
		detail_section = self._detail_section_repository.get(id)
		return detail_section_to_data(detail_section)

	def update(self, id, fields):
		detail_section = self._detail_section_repository.get(id)

		title = fields.get('title')
		if title is not None:
			detail_section.set_title(title)

		self._unit_of_work.commit()

	def get_branch_for_node(self, id):
		detail_section = self._detail_section_repository.get(id)
		detail_section_node = NodeContent(model=detail_section, model_name='detail_section')
		nodes = [detail_section_node]
		node = detail_section_node
		while self.responds_to_get_parent(node.model):
			node = node.model.get_parent()
			nodes.insert(0, node)

		##flatten nodes to data somehow

	def responds_to_get_parent(self, model):
		return (hasattr(model, 'get_parent') and callable(model.get_parent))
