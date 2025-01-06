from aiogram import Bot, Dispatcher, types
import asyncio, logging, os
from dotenv import load_dotenv
from aiogram.filters import Command
from button.button import keybourd_main
from handlers.register import router as register
from handlers.command import router as command

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет пожалуйста пройдите регистрацию.", reply_markup=keybourd_main)

async def main():
    dp.include_router(register)
    dp.include_router(command)

    await dp.start_polling(bot)

asyncio.run(main())