from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.default import menu
from loader import dp
from states import GroupChoiceState
from utils.db_api import quick_commands as commands


@dp.message_handler(Text(equals=["TA-91", "TA-92"]), state=GroupChoiceState.group_choice_state)
async def show_group_choice(message: types.Message, state: FSMContext):
    group = message.text

    await message.answer(f"Ваша група: {group}", reply_markup=menu)
    await commands.add_user(id=message.from_user.id, name=message.from_user.full_name, group=group)
    await state.finish()
