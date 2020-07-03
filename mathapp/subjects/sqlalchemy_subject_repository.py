from mathapp.db_sqlalchemy import Session
from mathapp.subjects.orm_subject import ORMSubject
from mathapp.subjects.subject_mapper import SubjectMapper

class SQLAlchemySubjectRepository:
	
	def list(self):
		subjects = Session.query(ORMSubject).all()
		containers = map(lambda orm_subject: SubjectMapper(orm_subject), subjects)
		return map(lambda container: container.get_subject(), containers)

	def get(self, id):
		return Session.query(Subject).filter(Subject.id == id).first()