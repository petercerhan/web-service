from mathapp.curriculum.interactor.domain_to_data_transforms.topic import topic_to_data

def topic_complete_followup_item_dto_template_to_data(topic_complete_followup_item_dto_template):
    topic_data = topic_to_data(topic_complete_followup_item_dto_template.topic)
    return {'topic': topic_data,
            'type': topic_complete_followup_item_dto_template.type}