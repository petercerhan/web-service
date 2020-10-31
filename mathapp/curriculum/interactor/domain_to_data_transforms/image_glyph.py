
import base64

def image_glyph_to_data(image_glyph):
	image_data = image_glyph.get_image_data()
	image_data_base64 = base64.b64encode(image_data).decode('utf-8')
	return {'id': image_glyph.get_id(), 
			'position': image_glyph.get_position(), 
			'source_code_filename': image_glyph.get_source_code_filename(), 
			'image_data': image_data_base64,
			'type': image_glyph.get_type()}