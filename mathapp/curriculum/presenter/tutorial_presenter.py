from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class TutorialPresenter:

	def create_form(self, error=None):
		if error is not None:
			flash(error.message)
		return render_template('tutorials/create.html')
