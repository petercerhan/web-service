from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class DetailSectionPresenter:

	def present_update(self, detail_section, error=None):
		if error is not None:
			flash(error.message)
		return render_template('detail_sections/update.html', detail_section=detail_section)