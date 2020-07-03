from mathapp.db_sqlalchemy import Session
from mathapp.subjects.subject import Subject
from mathapp.subjects.subject_container import SubjectContainer

class SQLAlchemySubjectRepository:
	
	def list(self):
		subjects = Session.query(Subject).all()
		containers = map(lambda orm_subject: SubjectContainer(orm_subject), subjects)
		return map(lambda container: container.get_subject(), containers)

	def get(self, id):
		return Session.query(Subject).filter(Subject.id == id).first()