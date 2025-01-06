from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keybourd_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Регистрацию")]
    ],
    resize_keyboard=True
)