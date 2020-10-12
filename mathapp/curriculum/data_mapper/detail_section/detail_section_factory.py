from mathapp.curriculum.data_mapper.detail_section.orm_detail_section import ORMDetailSection

class DetailSectionFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields, position):
		title = fields.get('title')
		orm_detail_section = ORMDetailSection(position=position, 
											  title=title)
		detail_section = orm_detail_section.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_detail_section)
		return detail_section