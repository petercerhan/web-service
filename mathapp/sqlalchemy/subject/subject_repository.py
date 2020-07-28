from mathapp.sqlalchemy.subject.orm_subject import ORMSubject
from mathapp.library.errors.not_found_error import NotFoundError

class SubjectRepository:

	def __init__(self, unit_of_work, session):
		self._session = session
		self._unit_of_work = unit_of_work
	
	def list(self):
		orm_subjects = self._session.query(ORMSubject).all()
		subjects = [orm_subject.get_model(unit_of_work=self._unit_of_work) for orm_subject in orm_subjects]
		self._unit_of_work.register_queried(orm_subjects)
		return subjects

	def get(self, id):
		orm_subject = self._session.query(ORMSubject).filter(ORMSubject.id == id).first()

		if not orm_subject:
			raise NotFoundError(message = "Not Found")

		subject = orm_subject.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_subject])

		return subject
