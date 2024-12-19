from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MENU = ['эспрессо', "капучино", "Американо", "Латте", "3 в 1"]

keydord_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выбрать Напиток")],
    ],
    resize_keyboard=True
)

def genrate_menu_keybord():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=menu)] for menu in MENU ],
        resize_keyboard=True
    )

def keyboard_confirm():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Да")],
            [KeyboardButton(text="Нет")],
        ],
        resize_keyboard=True
    )