from werkzeug.security import check_password_hash, generate_password_hash

class EncryptionService:

	def generate_password_hash(self, password):
		return generate_password_hash(password)

	def check_password_hash(self, encrypted_password, check_password):
		return check_password_hash(encrypted_password, check_password)