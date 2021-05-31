
import base64

def diagram_exercise_to_data(diagram_exercise):
	image_data = diagram_exercise.get_diagram_image_data()
	diagram_image_data_base64 = base64.b64encode(image_data).decode('utf-8')
	return {'id': diagram_exercise.get_id(), 
			'type': diagram_exercise.get_type(), 
			'name': diagram_exercise.get_name(), 
			'tag': diagram_exercise.get_tag(),
			'text': diagram_exercise.get_text(), 
			'diagram_image_data': diagram_image_data_base64, 
			'source_code_filename': diagram_exercise.get_source_code_filename(), 
			'correct_option': diagram_exercise.get_correct_option(), 
			'incorrect_option_1': diagram_exercise.get_incorrect_option_1(), 
			'incorrect_option_2': diagram_exercise.get_incorrect_option_2(), 
			'incorrect_option_3': diagram_exercise.get_incorrect_option_3()}