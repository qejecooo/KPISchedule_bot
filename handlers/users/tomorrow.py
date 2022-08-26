from datetime import datetime
from aiogram import types
from aiogram.dispatcher import handler
from aiogram.dispatcher.filters import Text
from utils.db_api import quick_commands as commands
from loader import dp
from utils.misc.day_names import day_names
from utils.misc.get_normal_view import get_normal_view


@dp.message_handler(Text(equals=["Розклад на завтра ➡️"]))
async def tomorrow(message: types.Message):
    if datetime.today().weekday() + 1 == 3 or datetime.today().weekday() == 4 or datetime.today().weekday() == 5:
        await message.answer("<b> <i>Завтра</i> немає пар!</b>")
        handler.current_handler.reset()

    column_id = datetime.today().weekday() + 2

    if await commands.get_week_count() == 2:
        column_id = column_id + 5
        if column_id > 11:
            column_id = 1

    if await commands.get_group(id=message.from_user.id) == "TA-92":
        column_id = column_id + 11
        if column_id > 21:
            column_id = 12

    day_count = datetime.today().weekday() + 1
    if day_count == 7:
        day_count = 0

    one_day = await commands.select_one_column(column_id)
    text = f"<b>Розклад на</b> <i><b>{day_names[day_count]}:</b></i> \n" + await get_normal_view(one_day)

    await message.answer(text)
