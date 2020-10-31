from mathapp.curriculum.domain_model.detail_glyph import DetailGlyph
from mathapp.library.errors.validation_error import ValidationError

class ImageGlyph(DetailGlyph):

	def __init__(self, 
				 position, 
				 source_code_filename, 
				 image_data,
				 unit_of_work):
		self._source_code_filename = source_code_filename
		self._image_data = image_data
		self._unit_of_work = unit_of_work
		super().__init__(position, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._source_code_filename is None:
			raise ValidationError(message = f'ImageGlyph (id={self._id}) requires source_code_filename')

		if self._image_data is None:
			raise ValidationError(message = f'ImageGlyph (id={self._id}) requires image_data')

		super()._check_invariants()

	def get_source_code_filename(self):
		return self._source_code_filename

	def get_image_data(self):
		return self._image_data

	def get_type(self):
		return 'image_glyph'

	def __repr__(self):
		return f'<ImageGlyph(id={self._id}, source_code_filename={self._source_code_filename})>'