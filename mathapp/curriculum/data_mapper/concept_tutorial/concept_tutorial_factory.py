from mathapp.curriculum.data_mapper.concept_tutorial.orm_concept_tutorial import ORMConceptTutorial

class ConceptTutorialFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields, position):
		display_name = fields.get('display_name')
		orm_concept_tutorial = ORMConceptTutorial(position=position, 
												  complete_lesson=False, 
												  display_name=display_name)
		concept_tutorial = orm_concept_tutorial.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_concept_tutorial)

		return concept_tutorial