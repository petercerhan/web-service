

from mathapp.subjects.orm_subject import ORMSubject
from mathapp.subjects.subject_mapper import SubjectMapper

class SQLAlchemySubjectRepository:

	def __init__(self, unit_of_work, session):
		self._session = session
		self._unit_of_work = unit_of_work
	
	def list(self):
		subjects = self._session.query(ORMSubject).all()
		mappers = list(map(lambda orm_subject: SubjectMapper(self._unit_of_work, orm_subject), subjects))
		self._unit_of_work.register_queried(mappers)
		return list(map(lambda mapper: mapper.get_model(), mappers))

	def get(self, id):
		orm_subject = self._session.query(ORMSubject).filter(ORMSubject.id == id).first()
		mapper = SubjectMapper(self._unit_of_work, orm_subject)
		self._unit_of_work.register_queried([mapper])
		return mapper.get_model()