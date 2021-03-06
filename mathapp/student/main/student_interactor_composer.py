from mathapp.student.main.student_repository_composer import StudentRepositoryComposer
from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer

from mathapp.student.main.student_factory_composer import StudentFactoryComposer

from mathapp.student.interactor.course_push_control_interactor import CoursePushControlInteractor
from mathapp.student.interactor.student_interactor import StudentInteractor
from mathapp.student.interactor.student_course_interactor import StudentCourseInteractor
from mathapp.student.interactor.student_topic_interactor import StudentTopicInteractor

class StudentInteractorComposer:

    def __init__(self,
                 user_data,
                 infrastructure_service_composer,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._sqlalchemy_session = sqlalchemy_session
        self._infrastructure_service_composer = infrastructure_service_composer
        self._student_repository_composer = StudentRepositoryComposer(user_data=user_data,
                                                                      unit_of_work=unit_of_work,
                                                                      sqlalchemy_session=sqlalchemy_session)
        self._curriculum_repository_composer = CurriculumRepositoryComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)
        self._student_factory_composer = StudentFactoryComposer(user_data=user_data,
                                                                unit_of_work=unit_of_work)

    def compose_course_push_control_interactor(self):
        course_push_control_repository = self._student_repository_composer.compose_course_push_control_repository()
        return CoursePushControlInteractor(course_push_control_repository=course_push_control_repository,
                                           unit_of_work=self._unit_of_work)

    def compose_student_interactor(self):
        student_repository = self._student_repository_composer.compose_student_repository()
        student_course_repository = self._student_repository_composer.compose_student_course_repository()
        course_push_control_repository = self._student_repository_composer.compose_course_push_control_repository()
        course_repository = self._curriculum_repository_composer.compose_course_repository()
        student_course_factory = self._student_factory_composer.compose_student_course_factory()
        student_topic_factory = self._student_factory_composer.compose_student_topic_factory()
        return StudentInteractor(student_repository=student_repository,
                                 student_course_repository=student_course_repository,
                                 course_push_control_repository=course_push_control_repository,
                                 course_repository=course_repository,
                                 student_course_factory=student_course_factory,
                                 student_topic_factory=student_topic_factory,
                                 unit_of_work=self._unit_of_work)

    def compose_student_course_interactor(self):
        student_course_repository = self._student_repository_composer.compose_student_course_repository()
        student_topic_factory = self._student_factory_composer.compose_student_topic_factory()
        return StudentCourseInteractor(student_course_repository=student_course_repository,
                                       student_topic_factory=student_topic_factory,
                                       unit_of_work=self._unit_of_work)

    def compose_student_topic_interactor(self):
        student_topic_repository = self._student_repository_composer.compose_student_topic_repository()
        lesson_event_factory = self._student_factory_composer.compose_lesson_event_factory()
        exercise_event_factory = self._student_factory_composer.compose_exercise_event_factory()
        randomization_service = self._infrastructure_service_composer.compose_randomization_service()
        return StudentTopicInteractor(student_topic_repository=student_topic_repository,
                                      lesson_event_factory=lesson_event_factory,
                                      exercise_event_factory=exercise_event_factory,
                                      randomization_service=randomization_service,
                                      unit_of_work=self._unit_of_work)






