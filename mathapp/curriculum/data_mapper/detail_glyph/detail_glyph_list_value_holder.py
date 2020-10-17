

class DetailGlyphListValueHolder:

	def __init__(self, orm_model, unit_of_work):
		self._orm_model = orm_model
		self._unit_of_work = unit_of_work
		self._queried = False

	def get_list(self):
		orm_detail_glyphs = self._orm_model.detail_glyphs
		if not self._queried:
			self._unit_of_work.register_queried(orm_detail_glyphs)
		detail_glyphs = [x.get_model(unit_of_work=self._unit_of_work) for x in orm_detail_glyphs]
		self._queried = True
		return detail_glyphs

	def get_queried(self):
		return self._queried