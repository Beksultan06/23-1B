from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from button import keydord_main, MENU, genrate_menu_keybord, keyboard_confirm
import asyncio
from config import token

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет Добро пожаловать!", reply_markup=keydord_main)

@dp.message(F.text == 'Выбрать Напиток')
async def choose_drink(message:types.Message):
    keyboard = genrate_menu_keybord()
    await message.answer("Выберите напиток", reply_markup=keyboard)

@dp.message(F.text.in_(MENU))
async def drink_choice(message:types.Message):
    selected_drink = message.text
    await message.answer(f"Вы выбрали {selected_drink}. Хотите заказать этот напиток?", 
                         reply_markup=keyboard_confirm())

@dp.message(F.text == "Да")
async def da(message:types.Message):
    await message.answer("Ваш заказ подтвержден! Мы готовим ваш заказ ☕")

@dp.message(F.text == 'Нет')
async def no(message:types.Message):
    await message.answer("ваш заказ отменен")

async def main():
    print("Запукс Бота")
    await dp.start_polling(bot)

asyncio.run(main())