from mathapp.curriculum.interactor.domain_to_data_transforms.lesson import lesson_to_data


class LessonInteractor:
    
    def __init__(self, 
                lesson_repository, 
                lesson_factory, 
                unit_of_work_committer):
        self._lesson_repository = lesson_repository
        self._lesson_factory = lesson_factory
        self._unit_of_work_committer = unit_of_work_committer

    def list(self):
        lessons = self._lesson_repository.list()
        lessons_data = [lesson_to_data(lesson) for lesson in lessons]
        return lessons_data

    def create(self, fields):
        lesson = self._lesson_factory.create(fields)
        self._unit_of_work_committer.commit()
        return lesson