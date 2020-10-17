

def formula_glyph_to_data(formula_glyph):
	return {'id': formula_glyph.get_id(), 
			'position': formula_glyph.get_position(), 
			'formula': formula_glyph.get_formula(), 
			'type': formula_glyph.get_type()}