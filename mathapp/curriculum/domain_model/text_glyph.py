from mathapp.curriculum.domain_model.detail_glyph import DetailGlyph

class TextGlyph(DetailGlyph):

	def __init__(self, position, text, unit_of_work):
		self._text = text
		self._unit_of_work = unit_of_work
		super().__init__(position, unit_of_work)
		self._check_invariants()

	def _check_invariants(self):
		if self._text is None:
			raise ValidationError(message = "TextGlyph requires text")

		if not self._text.strip():
			raise ValidationError(message = f'Invalid text for TextGlyph (id={self._id})')

		super()._check_invariants()

	def get_text(self):
		return self._text

	def get_type(self):
		return 'text_glyph'

	def __repr__(self):
		return f'<TextGlyph(id={self._id}, text={self._text})>'