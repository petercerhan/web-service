from mathapp.library.errors.validation_error import ValidationError
from mathapp.library.errors.not_found_error import NotFoundError

class Tutorial:

    def __init__(self,
                 name,
                 lesson_value_holder,
                 tutorial_step_list_value_holder,
                 unit_of_work):
        self._id = None
        self._name = name
        self._lesson_value_holder = lesson_value_holder
        self._tutorial_step_list_value_holder = tutorial_step_list_value_holder
        self._unit_of_work = unit_of_work
        self._check_invariants()

    def _check_invariants(self):
        if not self._name:
            raise ValidationError(message="Tutorial requires name")

        if not self._name.strip():
            raise ValidationError(message="Invalid name for Tutorial")

        if not self._lesson_value_holder.get_set_at_init():
            raise ValidationError(message="Tutorial requires lesson")


    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self._check_invariants()
        self._unit_of_work.register_dirty(self)

    def get_lesson(self):
        return self._lesson_value_holder.get()

    def get_tutorial_steps(self):
        return self._tutorial_step_list_value_holder.get_list()

    def create_tutorial_step(self, tutorial_step_factory, fields):
        max_position = max([x.get_position() for x in self._tutorial_step_list_value_holder.get_list()], default=-1)
        next_position = max_position+1
        display_group = next_position
        tutorial_step = tutorial_step_factory.create(position=next_position,
                                                     display_group=display_group,
                                                     fields=fields)
        self._tutorial_step_list_value_holder.add(tutorial_step)
        return tutorial_step

    def sync_tutorial_step_positions(self, tutorial_steps_data_array):
        tutorial_steps = self._tutorial_step_list_value_holder.get_list()
        for data_item in tutorial_steps_data_array:
            tutorial_step = next(x for x in tutorial_steps if x.get_id() == data_item['id'])
            if tutorial_step is not None:
                tutorial_step.set_position(data_item['position'])

        self._adjust_display_groups(tutorial_steps)

    def _adjust_display_groups(self, tutorial_steps):
        sorted_tutorial_steps = sorted(tutorial_steps, key=lambda x: x.get_position())
        array_length = len(sorted_tutorial_steps)
        display_group_order_broken = False
        for index, tutorial_step in enumerate(sorted_tutorial_steps):
            if display_group_order_broken:                
                tutorial_step.set_display_group(sorted_tutorial_steps[index-1].get_display_group()+1)
            elif (index+1 < array_length) and ( tutorial_step.get_display_group() > sorted_tutorial_steps[index+1].get_display_group() ):
                display_group_order_broken = True
                if index == 0:
                    tutorial_step.set_display_group(0)
                else:
                    tutorial_step.set_display_group(sorted_tutorial_steps[index-1].get_display_group()+1)


    def get_tutorial_step(self, id):
        tutorial_steps = self._tutorial_step_list_value_holder.get_list()
        tutorial_step = next(x for x in tutorial_steps if x.get_id() == id)
        if tutorial_step is None:
            raise NotFoundError(message=f'Tutorial Step {id} not found on tutorial {self._id}')
        return tutorial_step

    def set_tutorial_step_display_group(self, tutorial_step_id, display_group):
        tutorial_steps = self._tutorial_step_list_value_holder.get_list()
        sorted_tutorial_steps = sorted(tutorial_steps, key=lambda x: x.get_position())
        final_index = len(sorted_tutorial_steps) - 1

        for index, tutorial_step in enumerate(sorted_tutorial_steps):
            if tutorial_step.get_id() == tutorial_step_id:
                if (index > 0) and (sorted_tutorial_steps[index-1].get_display_group() > display_group):
                    raise ValidationError(message=f'display_group must be greater than or equal to previous step display_group')
                if (index < final_index) and (display_group > sorted_tutorial_steps[index+1].get_display_group()):
                    raise ValidationError(message=f'display_group must be less than or equal to following step display_group')
                tutorial_step.set_display_group(display_group)

    def delete_tutorial_step(self, tutorial_step_id):
        tutorial_steps = self._tutorial_step_list_value_holder.get_list()
        deleted_position = None
        for tutorial_step in tutorial_steps:
            if tutorial_step.get_id() == tutorial_step_id:
                deleted_position = tutorial_step.get_position()
                tutorial_step.delete()
                self._tutorial_step_list_value_holder.remove_at_index(deleted_position)

        if deleted_position is None:
            return

        for tutorial_step in tutorial_steps:
            if tutorial_step.get_position() > deleted_position:
                prior_position = tutorial_step.get_position()
                tutorial_step.set_position(prior_position-1)

        self._check_invariants()
        self._unit_of_work.register_dirty(self)
        


    def delete(self):
        tutorial_steps = self._tutorial_step_list_value_holder.get_list()
        for tutorial_step in tutorial_steps:
            tutorial_step.delete()
        self._unit_of_work.register_deleted(self)

    def __repr__(self):
        return "<Tutorial(name='%s') ID(id='%s')>" % (self._name, self._id)



