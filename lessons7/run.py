import os, asyncio, logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.start import router as start
from app.student import router as student

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

async def main():
    dp.include_router(start)
    dp.include_router(student)

    await dp.start_polling(bot)

asyncio.run(main())