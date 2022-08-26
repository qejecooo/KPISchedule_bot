from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default import groups_list, menu
from loader import dp
from states import GroupChoiceState
from utils.db_api import quick_commands as commands


@dp.message_handler(Text(equals=["Змінити групу 🔄"]))
async def changegroup_query(message: types.Message):
    await GroupChoiceState.group_update_state.set()
    await message.answer("Введіть вашу групу: ", reply_markup=groups_list)


@dp.message_handler(Text(equals=["TA-91", "TA-92"]), state=GroupChoiceState.group_update_state)
async def changegroup(message: types.Message, state: FSMContext):
    group = message.text
    users = await commands.select_all_users()

    for user in users:
        if message.from_user.id == user.id:
            await commands.update_user_group(id=message.from_user.id, group=str(group))
            await message.answer(f"Ваша група: {group}", reply_markup=menu)
            await state.finish()
            break
