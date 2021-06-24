from mathapp.curriculum.data_mapper.tutorial.orm_tutorial import ORMTutorial
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError

class TutorialRepository:

	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def get(self, id):
		orm_tutorial = self._session.query(ORMTutorial).filter(ORMTutorial.id == id).first()

		if not orm_tutorial:
			raise NotFoundError(message=f'Tutorial id={id} not found')

		tutorial = orm_tutorial.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_tutorial])
		return tutorial

	