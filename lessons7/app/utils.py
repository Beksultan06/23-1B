import asyncio, os, logging
from datetime import datetime
from aiogram import Bot
from dotenv import load_dotenv
from app.states import student_data

load_dotenv()

bot = Bot(token=os.environ.get("token"))

async def schedule_task(deadline_time):
    now = datetime.now()
    delta = (deadline_time - now).total_seconds()

    if delta < 0:
        await bot.send_message(student_data['chat_id'], "Эта задание уже должно быть выполнена")
    else:
        await asyncio.sleep(delta)
        await task_to_perform()

async def task_to_perform():
    try:
        chat_id = student_data['chat_id']
        await bot.send_message(chat_id, f"Задание для {student_data['name']} выполнена")
    except Exception as e:
        logging.error(f"Ошибка: {e}")