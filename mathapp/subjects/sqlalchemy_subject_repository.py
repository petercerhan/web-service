from mathapp.db_sqlalchemy import Session
from mathapp.subjects.orm_subject import ORMSubject
from mathapp.subjects.subject_mapper import SubjectMapper

class SQLAlchemySubjectRepository:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work
	
	def list(self):
		subjects = Session.query(ORMSubject).all()
		mappers = map(lambda orm_subject: SubjectMapper(self._unit_of_work, orm_subject), subjects)
		return map(lambda mapper: mapper.get_model(), mappers)

	def get(self, id):
		orm_subject = Session.query(Subject).filter(Subject.id == id).first()
		mapper = SubjectMapper(orm_subject)
		return mapper.get_model()