from werkzeug.security import check_password_hash, generate_password_hash

import hashlib
import hmac
import base64

import sys

class EncryptionService:

	def __init__(self, csrf_hash_key):
		self._csrf_hash_key = csrf_hash_key.encode('utf-8')

	def generate_password_hash(self, password):
		return generate_password_hash(password)

	def check_password_hash(self, encrypted_password, check_password):
		return check_password_hash(encrypted_password, check_password)

	def generate_hash_for_csrf(self, message):
		encoded_message = message.encode('utf-8')
		message_hash = base64.b64encode(hmac.new(self._csrf_hash_key, encoded_message, digestmod=hashlib.sha256).digest())
		return message_hash.decode('utf-8')

	def check_hash_for_csrf(self, check_hash, message):
		encoded_check_hash = check_hash.encode('utf-8')
		encoded_message = message.encode('utf-8')
		message_hash = base64.b64encode(hmac.new(self._csrf_hash_key, encoded_message, digestmod=hashlib.sha256).digest())
		return hmac.compare_digest(message_hash, encoded_check_hash)

