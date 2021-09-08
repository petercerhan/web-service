

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

    def update_latest_student_course(self, student_id):
        json = self._request.get_json()
        student_course_id = json.get('id')
        student_course = self._student_interactor.update_latest_student_course(student_id=student_id, student_course_id=student_course_id)
        return student_course
