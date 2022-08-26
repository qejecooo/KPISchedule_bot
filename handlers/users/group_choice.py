from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import groups_list
from loader import dp


@dp.message_handler(Text(equals=["TA-91", "TA-92"]))
async def show_group_choice(message: types.Message):
    group = message.text
    await message.answer(f"Ваша група: {group}", reply_markup=ReplyKeyboardRemove())
