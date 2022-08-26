from datetime import datetime

from loader import bot
from utils.db_api import quick_commands as commands
from utils.misc.get_normal_view import get_normal_view


async def reminder_message(temp):
    users = await commands.select_all_users()

    for user in users:
        column_id = datetime.today().weekday() + 1

        if await commands.get_week_count() == 2:
            column_id = column_id + 5
        if await commands.get_group(id=user.id) == "TA-92":
            column_id = column_id + 11

        one_day = await commands.select_one_column(column_id)
        one_day_schedule = (await get_normal_view(one_day)).split("\n")
        lesson = one_day_schedule[int(temp)]

        try:
            int(lesson[0]) == int(temp) + 1
        except IndexError:
            print("No lesson")
            continue

        if int(lesson[0]) == int(temp) + 1 and int(lesson[0]) != "Вікно":
            await bot.send_message(chat_id=user.id, text="Пара через 5 хвилин, не забудь!")
