from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.system.domain_model.user_session_parameters import UserSessionParameters
import datetime

class User:

	def __init__(self, username, password, unit_of_work):
		self._id = None

		self._username = username
		self._password = password

		self._unit_of_work = unit_of_work

		self._check_invariants()

	def _check_invariants(self):
		if not self._username:
			raise ValidationError(message = "User requires username")

		if not self._username.strip():
			raise ValidationError(message = "Invalid username")

		if not self._password:
			raise ValidationError(message = "User requires password")

	def get_id(self):
		return self._id

	def get_username(self):
		return self._username

	def get_password(self):
		return self._password
	
	def get_session_parameters(self):
		return UserSessionParameters(expiration_period = datetime.timedelta(minutes=30),
									api_expiration_period = datetime.timedelta(minutes=30),
									api_refresh_expiration_period = datetime.timedelta(days=30),
									user_id = self._id,
									name = self._username)