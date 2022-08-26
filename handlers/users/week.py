from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from utils.db_api import quick_commands as commands
from utils.misc.day_names import day_names
from utils.misc.get_normal_view import get_normal_view


@dp.message_handler(Text(equals=["Розклад на тиждень 7⃣", "Розклад на наступний тиждень 🔜"]))
async def week(message: types.Message, start=1, end=6):
    _fn = "week"
    status, result = await commands.get_week_count()
    if not status:
        print(f"ERROR: {_fn} {result}")

    week_count = result
    text = message.text

    if text == "Розклад на наступний тиждень 🔜":
        if week_count == 1:
            week_count = 2
        else:
            week_count = 1

    if week_count == 2:
        start = start + 5
        end = end + 5
    if await commands.get_group(id=message.from_user.id) == "TA-92":
        start = start + 11
        end = end + 11

    temp = 0
    await message.answer(
        f"<i><b>Розклад на</b></i> <code>{week_count}</code> <i><b>тиждень</b></i>")
    for id in range(start, end):
        if id == 4 or id == 9 or id == 15 or id == 20:
            await message.answer(f"<i><b>У</b></i> <i><b>{day_names[temp]}</b></i> <b>немає пар!</b>")
            temp += 1
            continue

        one_day = await commands.select_one_column(id)
        text = f"<i><b>Розклад на</b></i> <i><b>{day_names[temp]}:</b></i> \n" + str(await get_normal_view(one_day))
        await message.answer(text)

        temp += 1
