from mathapp.curriculum.interactor.domain_to_data_transforms.detail_section import (detail_section_to_data, detail_section_to_enriched_data)
from mathapp.curriculum.interactor.domain_to_data_transforms.node_content import node_content_list_to_data
from mathapp.curriculum.domain_model.node_content import NodeContent
from mathapp.library.class_implements_method import class_implements_method

from mathapp.curriculum.interactor.domain_to_data_transforms.detail_glyph import detail_glyph_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.text_glyph import text_glyph_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.formula_glyph import formula_glyph_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.image_glyph import image_glyph_to_data

import sys

class DetailSectionInteractor:

	def __init__(self, 
				 detail_section_repository, 
				 text_glyph_factory, 
				 formula_glyph_factory, 
				 image_glyph_factory, 
				 file_service, 
				 date_service,
				 unit_of_work):
		self._detail_section_repository = detail_section_repository
		self._text_glyph_factory = text_glyph_factory
		self._formula_glyph_factory = formula_glyph_factory
		self._image_glyph_factory = image_glyph_factory
		self._file_service = file_service
		self._date_service = date_service
		self._unit_of_work = unit_of_work

	def read(self, id):
		detail_section = self._detail_section_repository.get(id)
		return detail_section_to_enriched_data(detail_section)

	def update(self, id, fields):
		detail_section = self._detail_section_repository.get(id)

		title = fields.get('title')
		if title is not None:
			detail_section.set_title(title)

		detail_glyphs = fields.get('detail_glyphs')
		if detail_glyphs is not None:
			detail_section.sync_detail_glyph_positions(detail_glyphs)

		self._unit_of_work.commit()
		return detail_section_to_enriched_data(detail_section)

	def get_branch_for_node(self, id):
		detail_section = self._detail_section_repository.get(id)
		detail_section_node = NodeContent(model=detail_section, model_name='detail_section')
		nodes = [detail_section_node]
		node = detail_section_node
		while class_implements_method(node.model, 'get_parent'):
			node = node.model.get_parent()
			nodes.insert(0, node)

		return node_content_list_to_data(nodes)

	def create_text_glyph(self, detail_section_id, fields):
		detail_section = self._detail_section_repository.get(detail_section_id)
		text_glyph = detail_section.create_detail_glyph(fields=fields, 
														detail_glyph_factory=self._text_glyph_factory)
		self._unit_of_work.commit()
		return text_glyph_to_data(text_glyph)

	def create_formula_glyph(self, detail_section_id, fields):
		detail_section = self._detail_section_repository.get(detail_section_id)
		formula_glyph = detail_section.create_detail_glyph(fields=fields, 
															detail_glyph_factory=self._formula_glyph_factory)
		self._unit_of_work.commit()
		return formula_glyph_to_data(formula_glyph)

	def create_image_glyph(self, user_id, detail_section_id, source_code_file, image_file, fields):
		detail_section = self._detail_section_repository.get(detail_section_id)

		filename = self._filename_for_source_code_file(user_id, source_code_file)
		self._file_service.upload_file(file=source_code_file, filename=filename)

		create_fields = {}
		create_fields['source_code_filename'] = filename
		create_fields['image_data'] = image_file.read()

		image_glyph = detail_section.create_detail_glyph(fields=create_fields, 
														 detail_glyph_factory=self._image_glyph_factory)

		self._unit_of_work.commit()
		return image_glyph_to_data(image_glyph)

	def read_detail_glyph(self, detail_section_id, detail_glyph_id):
		detail_section = self._detail_section_repository.get(detail_section_id)
		detail_glyph = detail_section.get_detail_glyph(detail_glyph_id)
		return detail_glyph_to_data(detail_glyph)

	def update_text_glyph(self, detail_section_id, text_glyph_id, fields):
		detail_section = self._detail_section_repository.get(detail_section_id)
		text_glyph = detail_section.get_detail_glyph(text_glyph_id)

		text = fields.get('text')
		if text is not None:
			text_glyph.set_text(text)

		self._unit_of_work.commit()
		return text_glyph_to_data(text_glyph)

	def update_formula_glyph(self, detail_section_id, formula_glyph_id, fields):
		detail_section = self._detail_section_repository.get(detail_section_id)
		formula_glyph = detail_section.get_detail_glyph(formula_glyph_id)

		formula = fields.get('formula')
		if formula is not None:
			formula_glyph.set_formula(formula)

		self._unit_of_work.commit()
		return formula_glyph_to_data(formula_glyph)

	def update_image_glyph(self, user_id, detail_section_id, image_glyph_id, source_code_file, image_file):
		detail_section = self._detail_section_repository.get(detail_section_id)
		image_glyph = detail_section.get_detail_glyph(image_glyph_id)

		self._file_service.delete_file(image_glyph.get_source_code_filename())
		new_filename = self._filename_for_source_code_file(user_id, source_code_file)
		self._file_service.upload_file(file=source_code_file, filename=new_filename)

		image_glyph.set_source_code_filename(new_filename)
		image_glyph.set_image_data(image_file.read())

		self._unit_of_work.commit()
		return image_glyph_to_data(image_glyph)

	def delete_detail_glyph(self, detail_section_id, detail_glyph_id):
		detail_section = self._detail_section_repository.get(detail_section_id)
		detail_glyph = detail_section.get_detail_glyph(detail_glyph_id)
		detail_section.delete_detail_glyph(detail_glyph_id=detail_glyph_id)

		if detail_glyph.get_type() == 'image_glyph':
			self._file_service.delete_file(detail_glyph.get_source_code_filename())

		self._unit_of_work.commit()
		return detail_glyph_to_data(detail_glyph)


	def _filename_for_source_code_file(self, user_id, source_code_file):
		file_extension = self._file_service.get_extension_for_filename(source_code_file.filename)
		datetime = self._date_service.current_datetime_utc()
		timestamp = self._date_service.format_datetime_as_timestamp(datetime)
		filename = f'ImageGlyphSourceCode_{user_id}_{timestamp}.{file_extension}'
		return filename

















