

class UserSessionData:

	def __init__(self, expiration_datetime, user_id, name):
		self.expiration_datetime = expiration_datetime
		self.user_id = user_id
		self.name = name