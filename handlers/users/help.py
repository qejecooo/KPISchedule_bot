from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Почати діалог",
            "/help - Отримати довідку",
            "/day - Вивести розклад на день",
            "/week - Вивести розклад на тиждень",
            "/changegroup - Змінити групу",)
    
    await message.answer("\n".join(text))
