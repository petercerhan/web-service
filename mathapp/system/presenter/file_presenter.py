from flask import (
    flash, redirect, url_for, render_template, abort, send_from_directory
)

import json

class FilePresenter:

	def __init__(self, file_service):
		self._file_service = file_service

	def file_download(self, filename):
		path = self._file_service.get_file_uploads_path()
		filename = self._file_service.secure_filename(filename)
		return send_from_directory(path, filename)
