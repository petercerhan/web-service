from flask import (
    flash, redirect, url_for, render_template, abort, make_response
)

class AuthPresenter:

	def present_register(self, error_message):
		if error_message is not None:
			flash(error_message)
		return render_template('auth/register.html')

	def present_register_successful(self):
		return redirect(url_for('auth.login'))

	def present_login(self, error_message):
		if error_message is not None:
			flash(error_message)
		return render_template('auth/login.html')

	def present_login_successful(self):
		test_response = 'test'
		return make_response(test_response)

		# return redirect(url_for('index'))