from mathapp.student.data_mapper.lesson_event.orm_lesson_event import ORMLessonEvent

class LessonEventFactory:

    def __init__(self,
                 user_data, 
                 unit_of_work):
        self._user_data = user_data
        self._unit_of_work = unit_of_work

    def create(self, fields):
        student_data = self._get_student()
        student_id = student_data.get('id')

        lesson_id = fields.get('lesson_id')
        completed = fields.get('completed')
        start_datetime = fields.get('start_datetime')
        end_datetime = fields.get('end_datetime')
        client_timezone = fields.get('client_timezone')
        activity_data = fields.get('activity_data')

        orm_lesson_event = ORMLessonEvent(student_id=student_id,
                                          lesson_id=lesson_id,
                                          completed=completed,
                                          start_datetime=start_datetime,
                                          end_datetime=end_datetime,
                                          client_timezone=client_timezone,
                                          activity_data=activity_data)
        self._unit_of_work.register_created(orm_lesson_event)
        lesson_event = orm_lesson_event.get_model(unit_of_work=self._unit_of_work)
        return lesson_event


    def _get_student(self):
        roles = self._user_data['roles']
        student = next(x for x in roles if x['type'] == 'student')
        if student is not None:
            return student
        else:
            raise MathAppError('LessonEventFactory cannot find student')

