from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sqlite3

from lessons6.db import DATABASE_PATH, init_db

router = Router()

class UserRegister(StatesGroup):
    last_name = State()
    first_name = State()
    gender = State()
    age = State()
    phone_number = State()
    email = State()

@router.message(F.text == "Регистрацию")
async def last_name(message:types.Message, state:FSMContext):
    await message.answer("Введите вашу фамилию: ")
    await state.set_state(UserRegister.last_name)

@router.message(UserRegister.last_name)
async def first_name(message:types.Message, state:FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Введите ваше имя: ")
    await state.set_state(UserRegister.first_name)

@router.message(UserRegister.first_name)
async def gender(message:types.Message, state:FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Ваш пол муж/жен")
    await state.set_state(UserRegister.gender)

@router.message(UserRegister.gender)
async def age(message:types.Message, state:FSMContext):
    if message.text.lower() not in ['муж', 'жен']:
        await message.answer("Пожалуйста, укажите пол как 'мужской' или 'женский'" )
        return
    await state.update_data(gender=message.text.lower())
    await message.answer("Ввадите ваш возраст")
    await state.set_state(UserRegister.age)

@router.message(UserRegister.age)
async def phone_number(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 17:
            await message.answer("Возраст должен быть больше 17 лет.")
            return
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст.")
        return
    await state.update_data(age=age)
    await message.answer("Введите ваш номер телефона: ")
    await state.set_state(UserRegister.phone_number)

@router.message(UserRegister.phone_number)
async def email(message: types.Message, state: FSMContext):
    if len(message.text) < 10 or not message.text.isdigit():
        await message.answer("Пожалуйста, введите корректный номер телефона.")
        return
    await state.update_data(phone_number=message.text)
    await message.answer("Введите вашу почту: ")
    await state.set_state(UserRegister.email)

@router.message(UserRegister.email)
async def finish_registration(message: types.Message, state: FSMContext):
    if "@" not in message.text or "." not in message.text:
        await message.answer("Пожалуйста, введите корректный адрес электронной почты.")
        return
    await state.update_data(email=message.text)
    user_data = await state.get_data()

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (last_name, first_name, gender, age, phone_number, email)
                   VALUES(?, ?, ?, ?, ?, ?)''',
                   (user_data['last_name'], user_data['first_name'], user_data['gender'], user_data['age'],
                    user_data['phone_number'], user_data['email']))
    conn.commit()
    conn.close()

    await message.answer(f"Регистрация завершена! Вот ваши данные:\n"
                         f"Фамилия: {user_data['last_name']}\n"
                         f"Имя: {user_data['first_name']}\n"
                         f"Пол: {user_data['gender']}\n"
                         f"Возраст: {user_data['age']}\n"
                         f"Телефон: {user_data['phone_number']}\n"
                         f"Почта: {user_data['email']}")
    await state.clear()

init_db()