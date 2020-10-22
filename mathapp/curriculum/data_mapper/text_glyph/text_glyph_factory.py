from mathapp.curriculum.data_mapper.text_glyph.orm_text_glyph import ORMTextGlyph

import sys

class TextGlyphFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields, position):
		print(f'create text glyph at {position}', file=sys.stderr)
		text = fields.get('text')
		orm_text_glyph = ORMTextGlyph(position=position, 
									  text=text)
		text_glyph = orm_text_glyph.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_text_glyph)
		return text_glyph
