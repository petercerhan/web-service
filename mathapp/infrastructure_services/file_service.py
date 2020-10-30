from werkzeug.utils import secure_filename
import os

class FileService:

	_extension_allowlist = {'txt', 'tex'}

	def __init__(self, file_uploads_path):
		self._file_uploads_path = file_uploads_path

	def upload_file(self, file, filename):
		extension = self.get_extension_for_filename(filename)
		if extension is None:
			return False
		if extension not in self._extension_allowlist:
			return False

		file_location = os.path.join(self._file_uploads_path, filename)
		file.save(file_location)

	def get_extension_for_filename(self, filename):
		if '.' not in filename:
			return None
		return filename.rsplit('.', 1)[1].lower()