from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Розклад на день 🌅"),
            KeyboardButton(text="Розклад на тиждень 7⃣"),
        ],
        [
            KeyboardButton(text="Розклад на завтра ➡️"),
            KeyboardButton(text="Розклад на наступний тиждень 🔜"),
        ],
        [
            KeyboardButton(text="Змінити групу 🔄"),
            KeyboardButton(text="Підтримати 💳"),
        ],
    ],

    resize_keyboard=True
)
