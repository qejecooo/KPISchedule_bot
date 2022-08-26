from loader import dp, bot
from utils.db_api.schemas.users import User


async def reminder_message():
    for user in User:
        await bot.send_message(chat_id=User.id, text="Пара через 5 хвилин, не забудь!")
