
from __future__ import print_function # In python 2.7
import sys

from mathapp.db import Session
from mathapp.subjects.orm_subject import ORMSubject
from mathapp.subjects.subject_mapper import SubjectMapper

class SQLAlchemySubjectRepository:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work
	
	def list(self):
		subjects = Session.query(ORMSubject).all()
		mappers = list(map(lambda orm_subject: SubjectMapper(self._unit_of_work, orm_subject), subjects))
		self._unit_of_work.register_queried(mappers)
		return list(map(lambda mapper: mapper.get_model(), mappers))

	def get(self, id):
		orm_subject = Session.query(ORMSubject).filter(ORMSubject.id == id).first()
		mapper = SubjectMapper(self._unit_of_work, orm_subject)
		self._unit_of_work.register_queried([mapper])
		return mapper.get_model()