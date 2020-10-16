

class NodeContent:

	def __init__(self, model, model_name):
		self.model = model
		self.model_name = model_name

	def __repr__(self):
		return f'NodeContent for model: {self.model}'