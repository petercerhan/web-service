from mathapp.curriculum.data_mapper.lesson_intro.orm_lesson_intro import ORMLessonIntro

class LessonIntroFactory:

	def __init__(self, unit_of_work):
		self._unit_of_work = unit_of_work

	def create(self, position):
		orm_lesson_intro = ORMLessonIntro(position=position,
										 complete_lesson=False, 
										 description='placeholder description')
		lesson_intro = orm_lesson_intro.get_model(self._unit_of_work)
		self._unit_of_work.register_created(orm_lesson_intro)

		return lesson_intro
