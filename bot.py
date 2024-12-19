from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

bot = Bot(token='7562108093:AAGRpqLX0gUf89hM-d5V9H0Oixjqx4XoqKU')
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет! Я Бот")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())