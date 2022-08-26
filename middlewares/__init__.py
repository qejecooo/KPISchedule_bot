from aiogram import Dispatcher

from loader import dp, scheduler
from .throttling import ThrottlingMiddleware
from.scheduler import SchedulerMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(SchedulerMiddleware(scheduler))
