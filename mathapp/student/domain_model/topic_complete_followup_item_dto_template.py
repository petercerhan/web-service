from mathapp.libraries.general_library.errors.validation_error import ValidationError

class TopicCompleteFollowupItemDtoTemplate:

    def __init__(self,
                 topic):
        self.topic = topic
        self.type = 'topic_complete_followup_item'
        self._check_invariants()

    def _check_invariants(self):
        if self.topic is None:
            raise ValidationError(message='TutorialCompleteFollowupItemDtoTemplate requires topic')