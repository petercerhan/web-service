

def detail_section_to_data(detail_section):
	return {'id': detail_section.get_id(), 
			'position': detail_section.get_position(), 
			'title': detail_section.get_title(), 
			'display_name': detail_section.get_title(),
			'type': detail_section.get_type()}