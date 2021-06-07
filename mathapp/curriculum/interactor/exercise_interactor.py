from mathapp.curriculum.interactor.domain_to_data_transforms.exercise import exercise_to_data
from mathapp.curriculum.interactor.domain_to_data_transforms.exercise_enriched import exercise_to_enriched_data
from mathapp.curriculum.interactor.domain_to_data_transforms.formula_exercise_enriched import formula_exercise_to_enriched_data
from mathapp.curriculum.interactor.domain_to_data_transforms.diagram_exercise_enriched import diagram_exercise_to_enriched_data

class ExerciseInteractor:

	def __init__(self,
				 topic_repository,
				 formula_exercise_factory,
				 diagram_exercise_factory,
				 exercise_repository,
				 file_service,
				 date_service,
				 unit_of_work):
		self._topic_repository = topic_repository
		self._formula_exercise_factory = formula_exercise_factory
		self._diagram_exercise_factory = diagram_exercise_factory
		self._exercise_repository = exercise_repository
		self._file_service = file_service
		self._date_service = date_service
		self._unit_of_work = unit_of_work


	def get(self, id):
		exercise = self._exercise_repository.get(id=id)
		return exercise_to_enriched_data(exercise)


	def create_formula_exercise(self, topic_id, fields):
		topic = self._topic_repository.get(id=topic_id)
		formula_exercise = topic.create_exercise(exercise_factory=self._formula_exercise_factory, fields=fields)
		self._unit_of_work.commit()
		return exercise_to_data(formula_exercise)


	def update_formula_exercise(self, id, fields):
		exercise = self._exercise_repository.get(id=id)

		name = fields.get('name')
		if name is not None:
			exercise.set_name(name)

		tag = fields.get('tag')
		if tag is not None:
			exercise.set_tag(tag)

		text = fields.get('text')
		if tag is not None:
			exercise.set_text(text)

		formula_latex = fields.get('formula_latex')
		if formula_latex is not None:
			exercise.set_formula_latex(formula_latex)

		correct_option = fields.get('correct_option')
		if correct_option is not None:
			exercise.set_correct_option(correct_option)

		incorrect_option_1 = fields.get('incorrect_option_1')
		if incorrect_option_1 is not None:
			exercise.set_incorrect_option_1(incorrect_option_1)

		incorrect_option_2 = fields.get('incorrect_option_2')
		if incorrect_option_2 is not None:
			exercise.set_incorrect_option_2(incorrect_option_2)

		incorrect_option_3 = fields.get('incorrect_option_3')
		if incorrect_option_3 is not None:
			exercise.set_incorrect_option_3(incorrect_option_3)

		self._unit_of_work.commit()
		return formula_exercise_to_enriched_data(exercise)


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


	def update_diagram_exercise(self, user_id, exercise_id, source_code_file, image_file, fields):
		exercise = self._exercise_repository.get(id=exercise_id)

		if source_code_file is not None and image_file is not None:
			print('will attempt source code file update', file=sys.stderr)
			new_filename = self._filename_for_source_code_file(user_id=user_id, source_code_file=source_code_file)
			self._file_service.upload_file(file=source_code_file, filename=new_filename)
			exercise.set_diagram_image(diagram_image_data=image_file.read(), source_code_filename=new_filename)

		name = fields.get('name')
		if name is not None:
			exercise.set_name(name)

		tag = fields.get('tag')
		if tag is not None:
			exercise.set_tag(tag)

		text = fields.get('text')
		if tag is not None:
			exercise.set_text(text)

		correct_option = fields.get('correct_option')
		if correct_option is not None:
			exercise.set_correct_option(correct_option)

		incorrect_option_1 = fields.get('incorrect_option_1')
		if incorrect_option_1 is not None:
			exercise.set_incorrect_option_1(incorrect_option_1)

		incorrect_option_2 = fields.get('incorrect_option_2')
		if incorrect_option_2 is not None:
			exercise.set_incorrect_option_2(incorrect_option_2)

		incorrect_option_3 = fields.get('incorrect_option_3')
		if incorrect_option_3 is not None:
			exercise.set_incorrect_option_3(incorrect_option_3)

		self._unit_of_work.commit()
		return diagram_exercise_to_enriched_data(exercise)


	def _filename_for_source_code_file(self, user_id, source_code_file):
		file_extension = self._file_service.get_extension_for_filename(source_code_file.filename)
		datetime = self._date_service.current_datetime_utc()
		timestamp = self._date_service.format_datetime_as_timestamp(datetime)
		filename = f'ImageTutorialStepSourceCode_{user_id}_{timestamp}.{file_extension}'
		return filename

	def delete(self, id):
		exercise = self._exercise_repository.get(id=id)
		exercise.delete()
		self._unit_of_work.commit()
		return id




