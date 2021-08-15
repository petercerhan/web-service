from mathapp.student.main.student_repository_composer import StudentRepositoryComposer
from mathapp.curriculum.main.curriculum_repository_composer import CurriculumRepositoryComposer

from mathapp.student.main.student_factory_composer import StudentFactoryComposer

from mathapp.student.interactor.course_push_control_interactor import CoursePushControlInteractor
from mathapp.student.interactor.student_interactor import StudentInteractor
from mathapp.student.interactor.student_course_interactor import StudentCourseInteractor

class StudentInteractorComposer:

    def __init__(self,
                 user_data,
                 unit_of_work,
                 sqlalchemy_session):
        self._unit_of_work = unit_of_work
        self._sqlalchemy_session = sqlalchemy_session
        self._student_repository_composer = StudentRepositoryComposer(user_data=user_data,
                                                                      unit_of_work=unit_of_work,
                                                                      sqlalchemy_session=sqlalchemy_session)
        self._curriculum_repository_composer = CurriculumRepositoryComposer(unit_of_work=unit_of_work,
                                                                            sqlalchemy_session=sqlalchemy_session)
        self._student_factory_composer = StudentFactoryComposer(unit_of_work=unit_of_work)

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
        return StudentCourseInteractor(student_course_repository=student_course_repository)