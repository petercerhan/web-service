from mathapp.student.interactor.domain_to_data_transforms.lesson_completable_dto_template import lesson_completable_dto_template_to_data
from mathapp.student.interactor.domain_to_data_transforms.lesson_complete_package_dto_template import lesson_complete_package_dto_template_to_data
from mathapp.student.domain_model.lesson_complete_package_dto_template import LessonCompletePackageDtoTemplate

class StudentTopicInteractor:

    def __init__(self,
                 student_topic_repository,
                 lesson_event_factory,
                 exercise_event_factory,
                 randomization_service,
                 unit_of_work):
        self._student_topic_repository = student_topic_repository
        self._lesson_event_factory = lesson_event_factory
        self._exercise_event_factory = exercise_event_factory
        self._randomization_service = randomization_service
        self._unit_of_work = unit_of_work

    def get_next_lesson_completable(self, student_topic_id):
        student_topic = self._student_topic_repository.get(student_topic_id=student_topic_id)
        lesson_completable_dto_template = student_topic.get_next_lesson_completable(randomization_service=self._randomization_service)
        return lesson_completable_dto_template_to_data(lesson_completable_dto_template)

    def complete_lesson(self, 
                        student_topic_id, 
                        lesson_event_fields,
                        exercise_event_fields_list):
        student_topic = self._student_topic_repository.get(student_topic_id=student_topic_id)
        followup_items = student_topic.complete_lesson(lesson_event_fields=lesson_event_fields,
                                                       exercise_event_fields_list=exercise_event_fields_list,
                                                       lesson_event_factory=self._lesson_event_factory,
                                                       exercise_event_factory=self._exercise_event_factory)

        self._unit_of_work.commit()
        lesson_complete_package_template = LessonCompletePackageDtoTemplate(student_topic=student_topic,
                                                                            lesson_followup_item_dto_templates=followup_items)

        return lesson_complete_package_dto_template_to_data(lesson_complete_package_template)



    def record_lesson_aborted(self, 
                              student_topic_id, 
                              lesson_event_fields,
                              exercise_event_fields_list):
        student_topic = self._student_topic_repository.get(student_topic_id=student_topic_id)
        student_topic.record_lesson_aborted(lesson_event_fields=lesson_event_fields,
                                            exercise_event_fields_list=exercise_event_fields_list,
                                            lesson_event_factory=self._lesson_event_factory,
                                            exercise_event_factory=self._exercise_event_factory)
        self._unit_of_work.commit()
