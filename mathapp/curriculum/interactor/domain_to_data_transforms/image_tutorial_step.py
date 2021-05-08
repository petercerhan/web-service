
import base64

def image_tutorial_step_to_data(image_tutorial_step):
	image_data = image_tutorial_step.get_image_data()
	image_data_base64 = base64.b64encode(image_data).decode('utf-8')
	return {'id': image_tutorial_step.get_id(), 
			'position': image_tutorial_step.get_position(), 
			'display_group': image_tutorial_step.get_display_group(), 
			'source_code_filename': image_tutorial_step.get_source_code_filename(), 
			'image_data': image_data_base64,
			'type': image_tutorial_step.get_type()}