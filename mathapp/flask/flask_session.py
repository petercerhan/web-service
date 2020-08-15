from flask import session

class FlaskSession:

	def reset_user_id(self, user_id):
		session.clear()
		session['user_id'] = user_id