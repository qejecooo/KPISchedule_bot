from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink
from loader import dp



@dp.message_handler(Text(equals=["Підтримати 💳"]))
async def support(message: types.Message):
    await message.answer(f"Автор <b>вмирає</b> з голоду, так як поки що не має роботи\n"
                         f"<b>Пожалійте бідосю</b> і киньте кілька гримен на поїсти...\n"
                         f"Дякую!\nmono: " +
                         hlink("4441114444577355", "https://send.monobank.ua/4gNcVzj4gc"), disable_web_page_preview=True)
