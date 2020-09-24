import weakref

class ConceptTutorialUnitOfWorkDecorator:

	def __init__(self, unit_of_work, orm_concept_tutorial):
		self._unit_of_work = unit_of_work
		self._orm_concept_tutorial = weakref.proxy(orm_concept_tutorial)

	def register_dirty(self, lesson_intro):
		self._orm_concept_tutorial.sync_fields()

	def register_deleted(self, lesson_intro):
		self._unit_of_work.register_deleted(self._orm_concept_tutorial)