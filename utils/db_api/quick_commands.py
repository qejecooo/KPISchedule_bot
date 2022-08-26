from asyncpg import UniqueViolationError

from utils.db_api.schemas.schedule import Schedule
from utils.db_api.schemas.temp_variables import TempVariable
from utils.db_api.schemas.users import User


async def select_all_columns() -> Schedule:
    """
    Select all columns from database.
    :return: DB instance containing all columns from database.
    """
    schedule = await Schedule.query.gino.all()
    return schedule


async def select_one_column(column_id: int) -> Schedule:
    """
    Select one column from database.
    :param column_id: ID of column to select.
    :return: DB instance containing one column from database.
    """
    column = await Schedule.query.where(Schedule.id == column_id).gino.first()
    return column


async def add_user(id: int, name: str, group: str):
    """
    Add user to database.
    :param id: ID of user.
    :param name: Name of user.
    :param group: Group of user.
    :return: True if user was added, False if user already exists.
    """
    try:
        user = User(id=id, name=name, group=group)
        await user.create()
    except UniqueViolationError:
        pass


async def get_group(id: int) -> Schedule:
    """
    Select one column from database.
    :param column_id: ID of column to select.
    :return: DB instance containing one column from database.
    """
    column = await User.query.where(User.id == id).gino.first()
    group = column.group
    return group


async def select_all_users() -> User:
    """
    Select all users from database.
    :return: DB instance containing all users from database.
    """
    users = await User.query.gino.all()
    return users


async def select_one_user(id: int) -> User:
    """
    Select one user from database.
    :param id: ID of user to select.
    :return: DB instance containing one user from database.
    """
    user = await User.query.where(User.id == id).gino.first()
    return user


async def get_week_count():
    """
    Get recent week_count
    :return: Recent week count
    """
    week_count = await TempVariable.query.where(TempVariable.variable == "week_count").gino.first()
    if week_count is None:
        return False, "No week_count found! Add a variable in database."

    week_count = week_count.value
    return True, week_count


async def update_user_group(group: str, id):
    """
    Update user group in database.
    :param group: Group of user.
    :param id: ID of user.
    """
    user = await User.get(id)
    await user.update(group=group).apply()


async def update_week_count():
    """
    Update week_count in database.
    """
    week_count = await TempVariable.get("week_count")
    week_count_value = week_count.value
    if week_count_value == 1:
        week_count_value = 2
    else:
        week_count_value = 1
    await week_count.update(value=week_count_value).apply()
