from mathapp.system.interactor.domain_to_data_transforms.role import role_to_data


def user_to_data(user):
	roles_data = course_topic_data = [role_to_data(x) for x in user.get_roles()]
	return {'id': user.get_id(), 
			'username': user.get_username(), 
			'roles': roles_data}

