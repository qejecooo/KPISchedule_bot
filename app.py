from aiogram import executor
import middlewares, filters, handlers
from loader import dp, db, scheduler
from utils.db_api import db_gino
from utils.misc.set_scheduled_jobs import set_scheduled_jobs
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    await db_gino.on_startup(dispatcher)

    await db.gino.create_all()

    await on_startup_notify(dispatcher)

    await set_scheduled_jobs()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
