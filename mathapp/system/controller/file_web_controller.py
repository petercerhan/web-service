from flask import (
    request, flash, redirect, url_for, render_template, abort
)

from mathapp.library.errors.mathapp_error import MathAppError

class FileWebController:

	def __init__(self,
				 request,
				 file_presenter):
		self._request = request
		self._file_presenter = file_presenter

	def get_file(self, filename):
		return self._file_presenter.file_download(filename=filename)
