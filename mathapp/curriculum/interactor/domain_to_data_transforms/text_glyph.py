

def text_glyph_to_data(text_glyph):
	return {'id': text_glyph.get_id(), 
			'position': text_glyph.get_position(), 
			'text': text_glyph.get_text(), 
			'type': text_glyph.get_type()}