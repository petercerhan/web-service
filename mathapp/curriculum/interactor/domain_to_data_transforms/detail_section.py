from mathapp.curriculum.interactor.domain_to_data_transforms.detail_glyph import detail_glyph_to_data


def detail_section_to_enriched_data(detail_section):
	fields = detail_section_to_data(detail_section)
	detail_glyphs = detail_section.get_detail_glyphs()
	fields['detail_glyphs'] = [detail_glyph_to_data(x) for x in detail_glyphs]
	return fields

def detail_section_to_data(detail_section):
	return {'id': detail_section.get_id(), 
			'position': detail_section.get_position(), 
			'title': detail_section.get_title(), 
			'display_name': detail_section.get_title(),
			'type': detail_section.get_type()}