

import json

class AuthApiPresenter:

	def auth_credentials(self, 
						 auth_token):
		response = {
			'auth_token': auth_token
		}

		return json.dumps(response)

	def error(self, error):
		return error.message