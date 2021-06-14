from mathapp.library.errors.validation_error import ValidationError

class ProblemSetGenerator:

	def __init__(self,
				 name,
				 exercise_list_value_holder,
				 lesson_value_holder,
				 unit_of_work):
		self._id = None
		self._name = name
		self._exercise_list_value_holder = exercise_list_value_holder
		self._lesson_value_holder = lesson_value_holder
		self._unit_of_work = unit_of_work
		self._check_invariants()

	def _check_invariants(self):
		if self._name is None:
			raise ValidationError(message = f'ProblemSetGenerator requires name (id={self._id})')

		if self._name.strip() == '':
			raise ValidationError(message = f'ProblemSetGenerator requires name (id={self._id})')

	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def set_name(self, name):
		self._name = name
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def get_exercises(self):
		return self._exercise_list_value_holder.get_list()

	def get_add_exercise_options(self):
		topic = self._lesson_value_holder.get().get_topic()
		current_exercise_ids = [x.get_id() for x in self._exercise_list_value_holder.get_list()]
		topic_exercises = topic.get_exercises()
		add_exercise_options = list(filter(lambda x: x.get_id() not in current_exercise_ids, topic_exercises))
		return add_exercise_options

	def add_exercise(self, exercise):
		self._exercise_list_value_holder.add(exercise)
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def remove_exercise(self, exercise_id):
		remove_index = -1
		for index, exercise in enumerate(self._exercise_list_value_holder.get_list()):
			if exercise.get_id() == exercise_id:
				remove_index = index
		self._exercise_list_value_holder.remove_at_index(index=remove_index)
		self._check_invariants()
		self._unit_of_work.register_dirty(self)

	def __repr__(self):
		return f'<ProblemSetGenerator(id={self._id}, name={self._name})>'


