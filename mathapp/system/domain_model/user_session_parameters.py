

class UserSessionParameters:

	def __init__(self, 
				 expiration_period,
				 refresh_expiration_period,
				 api_expiration_period,
				 api_refresh_expiration_period,
				 user_id, 
				 name):
		self.expiration_period = expiration_period
		self.refresh_expiration_period = refresh_expiration_period
		self.api_expiration_period = api_expiration_period
		self.api_refresh_expiration_period = api_refresh_expiration_period
		self.user_id = user_id
		self.name = name