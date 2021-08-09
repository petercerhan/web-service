

def role_to_data(role):
	return {'id': role.get_id(), 
			'type': role.get_type()}