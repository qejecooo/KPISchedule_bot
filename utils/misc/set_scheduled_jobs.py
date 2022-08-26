from aiogram.types import Message

from loader import scheduler
from utils.db_api import quick_commands as commands
from utils.misc.reminder import reminder_message
from utils.misc.week_update import week_update


async def set_scheduled_jobs():
    scheduler.add_job(reminder_message, 'cron', day_of_week='mon-fri', hour=8, minute=25, end_date='2022-06-30', args=('0'))
    scheduler.add_job(reminder_message, 'cron', day_of_week='mon-fri', hour=10, minute=20, end_date='2022-06-30', args=('1'))
    scheduler.add_job(reminder_message, 'cron', day_of_week='mon-fri', hour=12, minute=15, end_date='2022-06-30', args=('2'))
    scheduler.add_job(reminder_message, 'cron', day_of_week='mon-fri', hour=14, minute=10, end_date='2022-06-30', args=('3'))
    scheduler.add_job(reminder_message, 'cron', day_of_week='mon-fri', hour=16, minute=5, end_date='2022-06-30', args=('4'))
    scheduler.add_job(week_update, 'cron', day_of_week='sun', hour=12, minute=00, end_date='2022-06-30')
