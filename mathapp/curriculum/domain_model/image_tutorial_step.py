from mathapp.curriculum.domain_model.tutorial_step import TutorialStep
from mathapp.library.errors.validation_error import ValidationError

class ImageTutorialStep(TutorialStep):

	def __init__(self,
				 position,
				 display_group,
				 source_code_filename,
				 image_data,
				 unit_of_work):
		self._source_code_filename = source_code_filename
		self._image_data = image_data
		self._unit_of_work = unit_of_work
		super().__init__(position, display_group, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._source_code_filename is None:
			raise ValidationError(message = f'ImageGlyph (id={self._id}) requires source_code_filename')

		if self._image_data is None:
			raise ValidationError(message = f'ImageGlyph (id={self._id}) requires image_data')

		super()._check_invariants()

	def get_source_code_filename(self):
		return self._source_code_filename

	def set_source_code_filename(self, source_code_filename):
		self._source_code_filename = source_code_filename
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_image_data(self):
		return self._image_data

	def set_image_data(self, image_data):
		self._image_data = image_data
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_type(self):
		return 'image_tutorial_step'

	def __repr__(self):
		return f'<ImageTutorialStep(id={self._id}, source_code_filename={self._source_code_filename})>'