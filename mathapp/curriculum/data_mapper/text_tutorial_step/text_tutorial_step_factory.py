from mathapp.curriculum.data_mapper.text_tutorial_step.orm_text_tutorial_step import ORMTextTutorialStep

class TextTutorialStepFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, 
			   fields, 
			   position, 
			   tutorial, 
			   display_group):
		text = fields.get('text')
		orm_text_tutorial_step = ORMTextTutorialStep(position=position,
													 display_group=display_group,
													 text=text,
													 tutorial_id=tutorial._id)
		text_tutorial_step = orm_text_tutorial_step.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_text_tutorial_step)
		return text_tutorial_step

	