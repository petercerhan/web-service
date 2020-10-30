from mathapp.library.errors.validation_error import ValidationError

class ImageGlyph:

	def __init__(self, position, source_code_file_path, unit_of_work):
		self._source_code_file_path = source_code_file_path
		self._unit_of_work = unit_of_work
		super().__init__(position, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._source_code_file_path is None:
			raise ValidationError(message = f'ImageGlyph (id={self._id}) requires source_code_file_path')

		super()._check_invariants()

	def get_type(self):
		return 'image_glyph'

	def __repr__(self):
		return f'<ImageGlyph(id={self._id}, source_code_file_path={self._source_code_file_path})>'