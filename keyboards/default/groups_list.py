from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

groups_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TA-91"),
            KeyboardButton(text="TA-92"),
        ],
    ],
    resize_keyboard=True
)
