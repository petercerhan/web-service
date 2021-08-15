

class StudentApiController:

    def __init__(self,
                 request,
                 student_interactor):
        self._request = request
        self._student_interactor = student_interactor

    def initialize_student_course(self, student_id):
        json = self._request.get_json()
        course_id = json.get('course_id')
        return self._student_interactor.initialize_student_course(student_id=student_id, course_id=course_id)
