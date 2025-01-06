from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import sqlite3
import asyncio, logging, os, aiosmtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

bot = Bot(token=os.environ.get('token'))
dp = Dispatcher()

conn = sqlite3.connect("email.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL
        )
""")
conn.commit()

def save_email_to_db(email):
    cursor.execute('INSERT INTO users (email) VALUES (?)', (email,))
    conn.commit()

async def send_email(to_email, message_body):
    message = EmailMessage()
    message.set_content(message_body)
    message['Subject'] = "Сообщение от бота"
    message['From'] = SMTP_USER
    message['To'] = to_email
    message['Reply-To'] = 'romhasanov2@gmail.com'

    try:
        logging.info(f"Отправка сообщение на {to_email}")
        await aiosmtplib.send(
            message,
            hostname=SMTP_SERVER,
            port=SMTP_PORT,
            start_tls=True,
            username=SMTP_USER,
            password=SMTP_PASSWORD
        )
        logging.info("Успешно отправлена")
    except Exception as e:
        logging.error("Ошибка при отправке email: ", e)

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет я телеграмм бот который отправит сообщение на почту!")

@dp.message(lambda message: "gmail.com" in message.text)
async def email(message:types.Message):
    user_email = message.text
    save_email_to_db(user_email)

    await message.answer(f"Я отправил сообщение на адрес {user_email}")

    email_message = "Привет! это сообщение отправлена через бота."
    await send_email(user_email, email_message)
    await message.answer("Сообщение успешно отправлена.")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())