from mathapp.curriculum.data_mapper.lesson.orm_lesson import ORMProblemSetGenerator
from mathapp.library.errors.not_found_error import NotFoundError

class ProblemSetGeneratorRepository:

	def __init__(self, unit_of_work, session):
		self._unit_of_work = unit_of_work
		self._session = session

	def get(self, id):
		orm_problem_set_generator = self._session.query(ORMProblemSetGenerator).filter(ORMProblemSetGenerator.id == id).first()

		if not orm_problem_set_generator:
			raise NotFoundError(message=f'ProblemSetGenerator id={id} not found')

		problem_set_generator = orm_problem_set_generator.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_queried([orm_problem_set_generator])
		return problem_set_generator