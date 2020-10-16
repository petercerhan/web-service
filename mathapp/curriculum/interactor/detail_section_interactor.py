from mathapp.curriculum.interactor.domain_to_data_transforms.detail_section import detail_section_to_data

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

