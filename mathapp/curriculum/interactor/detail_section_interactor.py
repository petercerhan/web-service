from mathapp.curriculum.interactor.domain_to_data_transforms.detail_section import detail_section_to_data

import sys

class DetailSectionInteractor:

	def __init__(self, detail_section_repository):
		self._detail_section_repository = detail_section_repository

	def read(self, id):
		detail_section = self._detail_section_repository.get(id)
		return detail_section_to_data(detail_section)