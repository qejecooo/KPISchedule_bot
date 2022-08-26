from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import groups_list
from loader import dp
from states import GroupChoiceState


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer("Оберіть свою групу: ", reply_markup=groups_list)
    await GroupChoiceState.group_choice_state.set()
