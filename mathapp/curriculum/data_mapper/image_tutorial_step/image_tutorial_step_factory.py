from mathapp.curriculum.data_mapper.image_tutorial_step.orm_image_tutorial_step import ORMImageTutorialStep

class ImageTutorialStepFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self,
			   fields,
			   position, 
			   tutorial,
			   display_group):
		source_code_filename = fields.get('source_code_filename')
		image_data = fields.get('image_data')
		orm_image_tutorial_step = ORMImageTutorialStep(position=position,
													   display_group=display_group,
													   source_code_filename=source_code_filename,
													   image_data=image_data,
													   tutorial_id=tutorial.get_id())
		image_tutorial_step = orm_image_tutorial_step.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_image_tutorial_step)
		return image_tutorial_step
