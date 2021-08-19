from mathapp.libraries.general_library.errors.validation_error import ValidationError
from mathapp.student.domain_model.lesson_completable_dto_template import LessonCompletableDtoTemplate
from mathapp.student.domain_model.lesson_complete_followup_item_dto_template import LessonCompleteFollowupItemDtoTemplate
from mathapp.student.domain_model.topic_complete_followup_item_dto_template import TopicCompleteFollowupItemDtoTemplate

class StudentTopic:

    def __init__(self,
                 lessons_completed,
                 total_lessons,
                 completed,
                 topic_value_holder,
                 lesson_event_list_value_holder,
                 unit_of_work):
        self._id = None
        self._lessons_completed = lessons_completed
        self._total_lessons = total_lessons
        self._completed = completed
        self._topic_value_holder = topic_value_holder
        self._lesson_event_list_value_holder = lesson_event_list_value_holder
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

    def get_next_lesson_completable(self, randomization_service):
        next_lesson = self._calculate_next_lesson()
        tutorial = next_lesson.get_tutorial()

        problem_set_dto_template = self._get_problem_set_template(next_lesson=next_lesson, 
                                                                  randomization_service=randomization_service)

        lesson_completable_dto_template = LessonCompletableDtoTemplate(lesson=next_lesson,
                                                                       tutorial=tutorial,
                                                                       problem_set_dto_template=problem_set_dto_template)

        return lesson_completable_dto_template

    def _calculate_next_lesson(self):
        topic = self._topic_value_holder.get()
        lessons = topic.get_lessons()
        lessons.sort(key=lambda x: x.get_position())
        lesson_events = self._lesson_event_list_value_holder.get_list()
        completed_lesson_events = list(filter(lambda x: x.get_completed(), lesson_events))
        for lesson in lessons:
            lesson_event = next((x for x in completed_lesson_events if x.get_lesson_id() == lesson.get_id()), None)
            if lesson_event is None:
                return lesson
            if lesson_event.get_completed() == False:
                return lesson

        return lessons[0]

    def _get_problem_set_template(self, next_lesson, randomization_service):
        problem_set_generator = next_lesson.get_problem_set_generator()
        problem_set_dto_template = None
        if problem_set_generator is not None:
            problem_set_dto_template = problem_set_generator.generate_problem_set(randomization_service=randomization_service, 
                                                                                  student_topic=self)
        return problem_set_dto_template



    def complete_lesson(self,
                        lesson_event_fields,
                        exercise_event_fields_list,
                        lesson_event_factory,
                        exercise_event_factory):
        new_lesson_event = lesson_event_factory.create(fields=lesson_event_fields)
        self._create_exercise_events(exercise_event_fields_list=exercise_event_fields_list,
                                     exercise_event_factory=exercise_event_factory)
        self._cache_topic_progress(new_lesson_event=new_lesson_event)        
        followup_items = self._generate_followup_items(lesson_event_fields=lesson_event_fields)
        return followup_items

    def _create_exercise_events(self, 
                                exercise_event_fields_list,
                                exercise_event_factory):
        for fields in exercise_event_fields_list:
            exercise_event_factory.create(fields=fields)

    def _cache_topic_progress(self, new_lesson_event):
        self._lessons_completed = self._get_completed_lessons_count(new_lesson_event=new_lesson_event)
        self._total_lessons = self._get_total_lessons_count()
        self._unit_of_work.register_dirty(self)

    def _get_completed_lessons_count(self, new_lesson_event):
        completed_lesson_events = self._get_all_completed_lesson_events(new_lesson_event=new_lesson_event)
        return self._count_unique_lessons_for_lesson_events(lesson_events=completed_lesson_events)

    def _get_all_completed_lesson_events(self, new_lesson_event):
        existing_lesson_events = self._lesson_event_list_value_holder.get_list()
        completed_lesson_events = list(filter(lambda x: x.get_completed(), existing_lesson_events))
        completed_lesson_events.append(new_lesson_event)
        return completed_lesson_events

    def _count_unique_lessons_for_lesson_events(self, lesson_events):
        lesson_events_by_id = {}
        for lesson_event in lesson_events:
            if lesson_events_by_id.get(lesson_event.get_lesson_id()) is None:
                lesson_events_by_id[lesson_event.get_lesson_id()] = lesson_event
        unique_lesson_events = lesson_events_by_id.values()
        return len(unique_lesson_events)


    def _get_total_lessons_count(self):
        lessons = self._topic_value_holder.get().get_lessons()
        return len(lessons)

    def _generate_followup_items(self, lesson_event_fields):
        followup_items = []
        self._add_lesson_complete_followup_item(lesson_event_fields=lesson_event_fields,
                                                followup_items=followup_items)
        self._add_topic_complete_followup_item_if_needed(followup_items=followup_items)
        return followup_items

    def _add_lesson_complete_followup_item(self, lesson_event_fields, followup_items):
        lesson_id = lesson_event_fields.get('lesson_id')
        lessons = self._topic_value_holder.get().get_lessons()
        lesson = next(x for x in lessons if x.get_id() == lesson_id)
        lesson_complete_followup_item = LessonCompleteFollowupItemDtoTemplate(lesson=lesson)
        followup_items.append(lesson_complete_followup_item)

    def _add_topic_complete_followup_item_if_needed(self, followup_items):
        if self._lessons_completed == self._total_lessons:
            topic = self._topic_value_holder.get()
            topic_complete_followup_item = TopicCompleteFollowupItemDtoTemplate(topic=topic)
            followup_items.append(topic_complete_followup_item)



    def __repr__(self):
        return f'<StudentTopic(id={self._id})>'













