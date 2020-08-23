from mathapp.library.errors.validation_error import ValidationError

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
	