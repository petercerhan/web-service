import weakref

class SubjectUnitOfWorkDecorator:
	
	def __init__(self, unit_of_work, subject_mapper):
		self._unit_of_work = unit_of_work
		self._subject_mapper = weakref.ref(subject_mapper)

	def register_created(self, subject):
		pass