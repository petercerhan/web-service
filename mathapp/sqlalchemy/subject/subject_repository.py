from mathapp.sqlalchemy.subject.orm_subject import ORMSubject
from mathapp.sqlalchemy.subject.subject_mapper import SubjectMapper
from mathapp.domain.errors.not_found_error import NotFoundError

class SubjectRepository:

	def __init__(self, unit_of_work, session):
		self._session = session
		self._unit_of_work = unit_of_work
	
	def list(self):
		subjects = self._session.query(ORMSubject).all()
		mappers = [SubjectMapper(self._unit_of_work, orm_subject) for orm_subject in subjects]
		self._unit_of_work.register_queried(mappers)
		return [mapper.get_model() for mapper in mappers]

	def get(self, id):
		orm_subject = self._session.query(ORMSubject).filter(ORMSubject.id == id).first()

		if not orm_subject:
			raise NotFoundError(message = "Not Found")

		# mapper = SubjectMapper(self._unit_of_work, orm_subject)
		# self._unit_of_work.register_queried([mapper])

		subject = orm_subject.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_subject])

		return subject
