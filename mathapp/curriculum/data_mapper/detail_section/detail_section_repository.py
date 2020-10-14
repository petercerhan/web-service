from mathapp.curriculum.data_mapper.detail_section.orm_detail_section import ORMDetailSection
from mathapp.library.errors.not_found_error import NotFoundError

class DetailSectionRepository:

	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def get(self, id):
		orm_detail_section = self._session.query(ORMDetailSection).filter(ORMDetailSection.id == id).first()
		if orm_detail_section is None:
			raise NotFoundError(message=f'Detail Section (id={id}) not found')
		detail_section = orm_detail_section.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_detail_section])
		return detail_section