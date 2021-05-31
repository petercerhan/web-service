from mathapp.curriculum.data_mapper.diagram_exercise.orm_diagram_exercise import ORMDiagramExercise

class DiagramExerciseFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields):
		name = fields.get('name')
		tag = fields.get('tag')
		text = fields.get('text')
		diagram_image_data = fields.get('diagram_image_data')
		source_code_filename = fields.get('source_code_filename')
		correct_option = fields.get('correct_option')
		incorrect_option_1 = fields.get('incorrect_option_1')
		incorrect_option_2 = fields.get('incorrect_option_2')
		incorrect_option_3 = fields.get('incorrect_option_3')

		orm_diagram_exercise = ORMDiagramExercise(name=name,
												  tag=tag,
												  text=text,
												  diagram_image_data=diagram_image_data,
												  source_code_filename=source_code_filename,
												  correct_option=correct_option,
												  incorrect_option_1=incorrect_option_1,
												  incorrect_option_2=incorrect_option_2,
												  incorrect_option_3=incorrect_option_3)
		diagram_exercise = orm_diagram_exercise.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_diagram_exercise)
		return diagram_exercise


		