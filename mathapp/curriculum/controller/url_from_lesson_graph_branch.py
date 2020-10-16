

def url_from_lesson_graph_branch(nodes):
	url = ''
	for node in nodes:
		url += '/'
		url += node['model_name']
		url += 's'
		url += '/'
		url += f"{node['model']['id']}"

	return url