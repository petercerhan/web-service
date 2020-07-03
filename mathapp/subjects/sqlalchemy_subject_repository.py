from mathapp.db_sqlalchemy import Session
from mathapp.subjects.orm_subject import ORMSubject
from mathapp.subjects.subject_mapper import SubjectMapper

class SQLAlchemySubjectRepository:
	
	def list(self):
		subjects = Session.query(ORMSubject).all()
		mappers = map(lambda orm_subject: SubjectMapper(orm_subject), subjects)
		return map(lambda mapper: mapper.get_subject(), mappers)

	def get(self, id):
		orm_subject = Session.query(Subject).filter(Subject.id == id).first()
		mapper = SubjectMapper(orm_subject)
		return mapper.get_subject()