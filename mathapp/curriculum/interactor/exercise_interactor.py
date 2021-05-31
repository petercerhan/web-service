from mathapp.curriculum.interactor.domain_to_data_transforms.exercise import exercise_to_data

class ExerciseInteractor:

	def __init__(self,
				 topic_repository,
				 formula_exercise_factory,
				 diagram_exercise_factory,
				 file_service,
				 date_service,
				 unit_of_work):
		self._topic_repository = topic_repository
		self._formula_exercise_factory = formula_exercise_factory
		self._diagram_exercise_factory = diagram_exercise_factory
		self._file_service = file_service
		self._date_service = date_service
		self._unit_of_work = unit_of_work

	def create_formula_exercise(self, topic_id, fields):
		topic = self._topic_repository.get(id=topic_id)
		formula_exercise = topic.create_exercise(exercise_factory=self._formula_exercise_factory, fields=fields)
		self._unit_of_work.commit()
		return exercise_to_data(formula_exercise)

	def create_diagram_exercise(self, user_id, topic_id, source_code_file, image_file, fields):		
		topic = self._topic_repository.get(id=topic_id)

		filename = self._filename_for_source_code_file(user_id=user_id, source_code_file=source_code_file)
		self._file_service.upload_file(file=source_code_file, filename=filename)

		create_fields = fields
		create_fields['source_code_filename'] = filename
		create_fields['diagram_image_data'] = image_file.read()

		diagram_exercise = topic.create_exercise(exercise_factory=self._diagram_exercise_factory, fields=create_fields)
		self._unit_of_work.commit()
		return exercise_to_data(diagram_exercise)


	def _filename_for_source_code_file(self, user_id, source_code_file):
		file_extension = self._file_service.get_extension_for_filename(source_code_file.filename)
		datetime = self._date_service.current_datetime_utc()
		timestamp = self._date_service.format_datetime_as_timestamp(datetime)
		filename = f'ImageTutorialStepSourceCode_{user_id}_{timestamp}.{file_extension}'
		return filename

