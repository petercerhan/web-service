from mathapp.curriculum.data_mapper.exercise.orm_exercise import ORMExercise
from mathapp.libraries.general_library.errors.not_found_error import NotFoundError

class ExerciseRepository:

	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def get(self, id):
		orm_exercise = self._session.query(ORMExercise).filter(ORMExercise.id == id).first()

		if not orm_exercise:
			raise NotFoundError(message=f'Exercise id={id} not found')

		exercise = orm_exercise.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_exercise])

		return exercise