from mathapp.curriculum.data_mapper.image_glyph.orm_image_glyph import ORMImageGlyph

class ImageGlyphFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields, position):
		source_code_filename = fields.get('source_code_filename')
		orm_image_glyph = ORMImageGlyph(position=position, 
										source_code_filename=source_code_filename)
		image_glyph = orm_image_glyph.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_image_glyph)
		return image_glyph