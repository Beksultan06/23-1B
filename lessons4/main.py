from aiogram import Dispatcher, types, Bot
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio, logging, os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

class UserRegister(StatesGroup):
    name = State()
    phone = State()
    course = State()
    departament = State()
    city = State()

student_data = {}

@dp.message(Command("start"))
async def start(message:types.Message, state:FSMContext):
    await message.answer("Привет, Введите свое имя.")
    await state.set_state(UserRegister.name)

@dp.message(UserRegister.name)
async def name(message:types.Message, state:FSMContext):
    student_data["name"] = message.text
    await message.reply("Введите номер телефона")
    await state.set_state(UserRegister.phone)

@dp.message(UserRegister.phone)
async def phone(message:types.Message, state:FSMContext):
    student_data['phone'] = message.text
    await message.reply("На каком курсе вы учитесь")
    await state.set_state(UserRegister.course)

@dp.message(UserRegister.course)
async def course(message:types.Message, state:FSMContext):
    student_data['course'] = message.text
    await message.reply("На каком направление вы учитесь")
    await state.set_state(UserRegister.departament)

@dp.message(UserRegister.departament)
async def departament(message:types.Message, state:FSMContext):
    student_data['departament'] = message.text
    await message.reply("Каком городе вы живете")
    await state.set_state(UserRegister.city)

@dp.message(UserRegister.city)
async def city(message:types.Message, state:FSMContext):
    student_data['city'] = message.text
    await message.answer(f"""Спасибо за информацию! Вот твой данные: \n
                         Имя: {student_data['name']}\n
                         Телефон: {student_data['phone']}\n
                         Курc : {student_data['course']}\n
                         Направление : {student_data['departament']}\n
                         Город : {student_data['city']}
                         """)
    await state.clear()

async def main():
    await dp.start_polling(bot)

asyncio.run(main())