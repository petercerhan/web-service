import json
import datetime

class AuthApiPresenter:

	def login_package(self, auth_token, auth_token_payload, user):
		expiration_utc = datetime.datetime.utcfromtimestamp(auth_token_payload['exp'])
		expiration_datetime = expiration_utc.strftime("%Y-%m-%d %H:%M:%S")
		refresh_expiration_datetime = auth_token_payload['refresh_exp'].strftime("%Y-%m-%d %H:%M:%S")

		auth_token_package = {
			'auth_token': auth_token,
			'expiration_datetime': expiration_datetime,
			'refresh_expiration_datetime': refresh_expiration_datetime
		}

		login_package = {
			'auth_token_package': auth_token_package,
			'user':	user
		}

		return json.dumps(login_package)


	def error(self, error):
		return error.message