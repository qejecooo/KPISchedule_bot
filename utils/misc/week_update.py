from utils.db_api import quick_commands as commands


async def week_update():
    await commands.update_week_count()
