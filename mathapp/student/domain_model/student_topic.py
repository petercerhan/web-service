from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.student.domain_model.lesson_completable_dto_template import LessonCompletableDtoTemplate
from mathapp.student.domain_model.lesson_complete_followup_item_dto_template import LessonCompleteFollowupItemDtoTemplate

class StudentTopic:

    def __init__(self,
                 lessons_completed,
                 total_lessons,
                 completed,
                 topic_value_holder,
                 unit_of_work):
        self._id = None
        self._lessons_completed = lessons_completed
        self._total_lessons = total_lessons
        self._completed = completed
        self._topic_value_holder = topic_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if self._lessons_completed is None:
            raise ValidationError(message='StudentTopic requires lessons_completed')

        if self._total_lessons is None:
            raise ValidationError(message='StudentTopic requires total_lessons')

        if self._completed is None:
            raise ValidationError(message='StudentTopic requires completed')

        if not self._topic_value_holder.get_set_at_init():
            raise ValidationError(message='StudentTopic requires topic')


    def get_id(self):
        return self._id

    def get_lessons_completed(self):
        return self._lessons_completed

    def get_total_lessons(self):
        return self._total_lessons

    def get_completed(self):
        return self._completed

    def get_topic(self):
        return self._topic_value_holder.get()

    def get_next_lesson_completable(self):
        topic = self._topic_value_holder.get()
        lessons = topic.get_lessons()
        next_lesson = lessons[0]
        tutorial = next_lesson.get_tutorial()
        
        problem_set_generator = next_lesson.get_problem_set_generator()
        problem_set_dto_template = None
        if problem_set_generator is not None:
            problem_set_dto_template = problem_set_generator.generate_problem_set(randomization_service=None, student_topic=self)


        lesson_completable_dto_template = LessonCompletableDtoTemplate(lesson=next_lesson,
                                                                       tutorial=tutorial,
                                                                       problem_set_dto_template=problem_set_dto_template)

        return lesson_completable_dto_template

    def complete_lesson(self,
                        lesson_event_fields,
                        lesson_event_factory):
        lesson_event_factory.create(fields=lesson_event_fields)

        ##Recalculate lessons completed etc.

        ##Create exercise events

        ##generate lesson complete package
        lesson_id = lesson_event_fields.get('lesson_id')
        lessons = self._topic_value_holder.get().get_lessons()
        import sys
        print(f'lessons: {lessons}', file=sys.stderr)
        lesson = next(x for x in lessons if x.get_id() == lesson_id)
        lesson_complete_followup_item = LessonCompleteFollowupItemDtoTemplate(lesson=lesson)
        return [lesson_complete_followup_item]


    def __repr__(self):
        return f'<StudentTopic(id={self._id})>'













