from mathapp.curriculum.interactor.domain_to_data_transforms.tutorial_step import tutorial_step_to_data

class TutorialStepInteractor:

	def __init__(self,
				 tutorial_repository,
				 text_tutorial_step_factory,
				 formula_tutorial_step_factory,
				 image_tutorial_step_factory,
				 file_service,
				 date_service,
				 unit_of_work):
		self._tutorial_repository = tutorial_repository
		self._text_tutorial_step_factory = text_tutorial_step_factory
		self._formula_tutorial_step_factory = formula_tutorial_step_factory
		self._image_tutorial_step_factory = image_tutorial_step_factory
		self._file_service = file_service
		self._date_service = date_service
		self._unit_of_work = unit_of_work

	def create_text_tutorial_step(self, tutorial_id, fields):
		tutorial = self._tutorial_repository.get(tutorial_id)
		text_tutorial_step = tutorial.create_tutorial_step(self._text_tutorial_step_factory, fields)
		self._unit_of_work.commit()
		return tutorial_step_to_data(text_tutorial_step)

	def create_formula_tutorial_step(self, tutorial_id, fields):
		tutorial = self._tutorial_repository.get(tutorial_id)
		formula_tutorial_step = tutorial.create_tutorial_step(self._formula_tutorial_step_factory, fields)
		self._unit_of_work.commit()
		return tutorial_step_to_data(formula_tutorial_step)

	def create_image_tutorial_step(self, user_id, tutorial_id, source_code_file, image_file, fields):
		tutorial = self._tutorial_repository.get(tutorial_id)

		filename = self._filename_for_source_code_file(user_id, source_code_file)
		self._file_service.upload_file(file=source_code_file, filename=filename)

		create_fields = {}
		create_fields['source_code_filename'] = filename
		create_fields['image_data'] = image_file.read()

		image_tutorial_step = tutorial.create_tutorial_step(tutorial_step_factory=self._image_tutorial_step_factory, fields=create_fields)
		self._unit_of_work.commit()
		return tutorial_step_to_data(image_tutorial_step)


	def read(self, tutorial_id, tutorial_step_id):
		tutorial = self._tutorial_repository.get(tutorial_id)
		tutorial_step = tutorial.get_tutorial_step(tutorial_step_id)
		return tutorial_step_to_data(tutorial_step)

	def update_text_tutorial_step(self, tutorial_id, tutorial_step_id, fields):
		tutorial = self._tutorial_repository.get(tutorial_id)
		tutorial_step = tutorial.get_tutorial_step(id=tutorial_step_id)

		display_group = fields.get('display_group')
		if display_group is not None:
			tutorial.set_tutorial_step_display_group(tutorial_step_id=tutorial_step_id, display_group=display_group)

		text = fields.get('text')
		if text is not None:
			tutorial_step.set_text(text)

		self._unit_of_work.commit()
		return tutorial_step_to_data(tutorial_step)

	def update_formula_tutorial_step(self, tutorial_id, tutorial_step_id, fields):
		tutorial = self._tutorial_repository.get(tutorial_id)
		tutorial_step = tutorial.get_tutorial_step(id=tutorial_step_id)

		display_group = fields.get('display_group')
		if display_group is not None:
			tutorial.set_tutorial_step_display_group(tutorial_step_id=tutorial_step_id, display_group=display_group)

		formula_latex = fields.get('formula_latex')
		if formula_latex is not None:
			tutorial_step.set_formula_latex(formula_latex)

		self._unit_of_work.commit()
		return tutorial_step_to_data(tutorial_step)

	def update_image_tutorial_step(self, user_id, tutorial_id, tutorial_step_id, source_code_file, image_file, fields):
		tutorial = self._tutorial_repository.get(tutorial_id)
		tutorial_step = tutorial.get_tutorial_step(id=tutorial_step_id)

		if source_code_file is not None and image_file is not None:
			new_filename = self._filename_for_source_code_file(user_id=user_id, source_code_file=source_code_file)
			self._file_service.upload_file(file=source_code_file, filename=new_filename)
			tutorial_step.set_image(image_data=image_file.read(), source_code_filename=new_filename)

		display_group = fields.get('display_group')
		if display_group is not None:
			tutorial.set_tutorial_step_display_group(tutorial_step_id=tutorial_step_id, display_group=display_group)

		self._unit_of_work.commit()
		return tutorial_step_to_data(tutorial_step)


	def delete(self, tutorial_id, tutorial_step_id):
		tutorial = self._tutorial_repository.get(tutorial_id)
		tutorial.delete_tutorial_step(tutorial_step_id=tutorial_step_id)
		self._unit_of_work.commit()
		return tutorial_step_id



	def _filename_for_source_code_file(self, user_id, source_code_file):
		file_extension = self._file_service.get_extension_for_filename(source_code_file.filename)
		datetime = self._date_service.current_datetime_utc()
		timestamp = self._date_service.format_datetime_as_timestamp(datetime)
		filename = f'ImageTutorialStepSourceCode_{user_id}_{timestamp}.{file_extension}'
		return filename





