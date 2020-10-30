from werkzeug.utils import secure_filename
from mathapp.library.errors.mathapp_error import MathAppError
import os

class FileService:

	_extension_allowlist = {'txt', 'tex'}

	def __init__(self, file_uploads_path):
		self._file_uploads_path = file_uploads_path

	def upload_file(self, file, filename):
		extension = self.get_extension_for_filename(filename)
		if extension is None:
			raise MathAppError(message='No file extension found')
		if extension not in self._extension_allowlist:
			raise MathAppError(message='File type not allowed')

		filename = secure_filename(filename)

		file_location = os.path.join(self._file_uploads_path, filename)
		file.save(file_location)

	def get_extension_for_filename(self, filename):
		if '.' not in filename:
			return None
		return filename.rsplit('.', 1)[1].lower()