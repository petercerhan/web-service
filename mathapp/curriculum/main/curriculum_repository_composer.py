from mathapp.curriculum.data_mapper.course.course_repository import CourseRepository
from mathapp.curriculum.data_mapper.topic.topic_repository import TopicRepository
from mathapp.curriculum.data_mapper.lesson.lesson_repository import LessonRepository
from mathapp.curriculum.data_mapper.tutorial.tutorial_repository import TutorialRepository
from mathapp.curriculum.data_mapper.exercise.exercise_repository import ExerciseRepository
from mathapp.curriculum.data_mapper.problem_set_generator.problem_set_generator_repository import ProblemSetGeneratorRepository

class CurriculumRepositoryComposer:

    def __init__(self,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._sqlalchemy_session = sqlalchemy_session

    def compose_course_repository(self):
        return CourseRepository(unit_of_work=self._unit_of_work,
                                session=self._sqlalchemy_session)

    def compose_topic_repository(self):
        return TopicRepository(unit_of_work=self._unit_of_work,
                               session=self._sqlalchemy_session)

    def compose_lesson_repository(self):
    	return LessonRepository(unit_of_work=self._unit_of_work,
    							session=self._sqlalchemy_session)

    def compose_tutorial_repository(self):
        return TutorialRepository(unit_of_work=self._unit_of_work,
                                  session=self._sqlalchemy_session)

    def compose_exercise_repository(self):
        return ExerciseRepository(unit_of_work=self._unit_of_work,
                                  session=self._sqlalchemy_session)

    def compose_problem_set_generator_repository(self):
        return ProblemSetGeneratorRepository(unit_of_work=self._unit_of_work,
                                             session=self._sqlalchemy_session)


