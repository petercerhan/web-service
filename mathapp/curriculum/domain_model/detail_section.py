from mathapp.curriculum.domain_model.instruction_section import InstructionSection
from mathapp.library.errors.validation_error import ValidationError

class DetailSection(InstructionSection):

	def __init__(self, 
				 position, 
				 title, 
				 parent_value_holder, 
				 detail_glyph_list_value_holder,
				 unit_of_work):
		self._title = title
		self._detail_glyph_list_value_holder = detail_glyph_list_value_holder
		self._unit_of_work = unit_of_work

		super().__init__(position, parent_value_holder, unit_of_work)

		self._check_invariants()

	def _check_invariants(self):
		if not self._title:
			raise ValidationError(message = "DetailSection requires title")

		if self._detail_glyph_list_value_holder.get_queried():
			self._check_detail_glyphs_valid_order()

		super()._check_invariants()

	def _check_detail_glyphs_valid_order(self):
		detail_glyphs = self._detail_glyph_list_value_holder.get_list()
		positions = [x.get_position() for x in detail_glyphs]
		if len(positions) > len(set(positions)):
			raise ValidationError(message = "DetailGlyphs for DetailSection must have unique positions")

	def get_title(self):
		return self._title

	def set_title(self, title):
		self._title = title
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_type(self):
		return 'detail_section'

	def get_detail_glyphs(self):
		return self._detail_glyph_list_value_holder.get_list()

	def sync_detail_glyph_positions(self, detail_glyph_data_array):
		detail_glyphs = self._detail_glyph_list_value_holder.get_list()
		for data_item in detail_glyph_data_array:
			detail_glyph = next(x for x in detail_glyphs if x.get_id() == data_item['id'])
			if detail_glyph is not None:
				detail_glyph.set_position(data_item['position'])

		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def create_detail_glyph(self, fields, detail_glyph_factory):
		max_position = max([x.get_position() for x in self._detail_glyph_list_value_holder.get_list()], default=-1)
		detail_glyph = detail_glyph_factory.create(fields=fields, position=max_position+1)
		self._detail_glyph_list_value_holder.add(detail_glyph)
		self._check_invariants()
		self._unit_of_work.register_dirty(self)
		return detail_glyph

	def get_detail_glyph(self, id):
		detail_glyphs = self._detail_glyph_list_value_holder.get_list()
		detail_glyph = next(x for x in detail_glyphs if x.get_id() == id)
		if detail_glyph is None:
			raise NotFoundError(message=f'Detail Glyph {id} not found on glyph {self._id}')
		return detail_glyph

	def delete_detail_glyph(self, detail_glyph_id):
		detail_glyphs = self._detail_glyph_list_value_holder.get_list()
		deleted_position = None
		for detail_glyph in detail_glyphs:
			if detail_glyph.get_id() == detail_glyph_id:
				deleted_position = detail_glyph.get_position()
				self._detail_glyph_list_value_holder.remove_at_index(deleted_position)
				detail_glyph.delete()

		if deleted_position is None:
			return 

		for detail_glyph in detail_glyphs:
			if detail_glyph.get_position() > deleted_position:
				prior_position = detail_glyph.get_position()
				detail_glyph.set_position(prior_position-1)

		self._check_invariants()
		self._unit_of_work.register_dirty(self)


	def __repr__(self):
		return f'<DetailSection(id={self._id}, title={self._title})>'














