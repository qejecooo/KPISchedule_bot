from aiogram.dispatcher.filters.state import StatesGroup, State


class GroupChoiceState(StatesGroup):
    group_choice_state = State()
    group_update_state = State()
