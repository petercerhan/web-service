

def image_glyph_to_data(image_glyph):
	return {'id': image_glyph.get_id(), 
			'position': image_glyph.get_position(), 
			'source_code_filename': image_glyph.get_source_code_filename(), 
			'type': image_glyph.get_type()}