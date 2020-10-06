from flask import request
from mathapp.library.errors.validation_error import ValidationError

class ConceptTutorialWebController:

    def __init__(self, 
                request, 
                presenter, 
                interactor):
        self._request = request
        self._presenter = presenter
        self._interactor = interactor

    def handle_create_request(self, lesson_id):
        if self._request.method == 'POST':
            return self._post_create_form(lesson_id=lesson_id)
        else:
            return self._get_create_form()

    def _post_create_form(self, lesson_id):
        fields = {}
        fields['display_name'] = self._request.form.get('display_name')

        try:
            self._interactor.create(fields=fields, lesson_id=lesson_id)
            return self._presenter.present_create_successful(lesson_id=lesson_id)
        except ValidationError as error:
            return self._presenter.present_create(error=error)

    def _get_create_form(self):
        return self._presenter.present_create()