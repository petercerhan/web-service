from mathapp.curriculum.interactor.domain_to_data_transforms.text_glyph import text_glyph_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.formula_glyph import formula_glyph_to_data

def detail_glyph_to_data(detail_glyph):
	type = detail_glyph.get_type()
	if type == 'text_glyph':
		return text_glyph_to_data(detail_glyph)
	if type == 'formula_glyph':
		return formula_glyph_to_data(detail_glyph)