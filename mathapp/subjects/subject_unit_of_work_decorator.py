import weakref

class SubjectUnitOfWorkDecorator:
	
	def __init__(self, subject_mapper):
		self._subject_mapper = weakref.ref(subject_mapper)