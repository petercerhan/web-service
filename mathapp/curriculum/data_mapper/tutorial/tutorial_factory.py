from mathapp.curriculum.data_mapper.tutorial.orm_tutorial import ORMTutorial

class TutorialFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, fields, lesson):
		orm_lesson = self._unit_of_work.orm_model_for_model(lesson)
		orm_tutorial = ORMTutorial(name=fields['name'])
		orm_lesson.tutorial=orm_tutorial

		tutorial = orm_tutorial.get_model(unit_of_work=self._unit_of_work)
		self._unit_of_work.register_created(orm_tutorial)
		return tutorial

