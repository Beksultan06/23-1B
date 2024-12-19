from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import token
import asyncio, random

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(messege:types.Message):
    await messege.answer("Привет Я бот\nЕсли хотите узнать какеи команлы есть /help")

@dp.message(Command("about"))
async def about(messege:types.Message):
    await messege.reply("Вы нажали на команду о нас")

@dp.message(Command("contacts"))
async def contact(message:types.Message):
    await message.answer("""
    Вы можете связаться с нами по следующим контактам:
    - Email: example@example.com
    - Телефон: +7 123 456 7890
""")

@dp.message(Command("locations"))
async def locations(message:types.Message):
    longitude = 72.7868
    latitude = 40.5269
    await message.answer("Локация города ош")
    await message.answer_location(latitude, longitude)

@dp.message(Command("gallery"))
async def gallery(message:types.Message):
    photos = [
        "https://triptokyrgyzstan.com/sites/default/files/styles/blog/public/media/image/kalachov_k._ala_too.jpg.webp?itok=pieYqbJE",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_UcbzOVEtzpiThlTe9udnaG2pOL1GIYXnTw&s"
    ]
    for photo in photos:
        await message.answer_photo(photo, caption="Фото из галерие")


@dp.message(Command("start_game"))
async def start_game(message:types.Message):
    await message.answer("Выберите число от 1 до 3: ")

@dp.message(Command("help"))
async def help(message:types.Message):
    await message.answer("Извините я не полне вас, доступные команды  \n /about - о нас \n /contacts - Наши контакты \n /locations - наша локация \n /gallery - Галлерия")

@dp.message()
async def play_game(message:types.Message):
    try:
        user_number = int(message.text.strip())
    except ValueError:
        return await message.answer("Выберите число от 1 до 3:")

    if user_number < 1 or user_number > 3:
        return await message.answer("Число должно быть от 1 до 3")

    bot_number = random.randint(1,3)

    if user_number == bot_number:
        result = "Ничья"
    elif user_number > bot_number:
        result = "Вы выиграли"
    else:
        result = "Вы проиграли"

    await message.answer(f"Ты выбрал {user_number}\nБот выбрал {bot_number}\n{result}")

async def main():
    print("Запуск бота")
    await dp.start_polling(bot)

asyncio.run(main())