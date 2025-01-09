from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from app.states import Student, student_data
from app.utils import schedule_task

router = Router()

@router.message(Student.name)
async def name(message:types.Message, state:FSMContext):
    student_data['name'] = message.text
    await message.reply("Введите ваш номер телефона")
    await state.set_state(Student.phone)

@router.message(Student.phone)
async def phone(message:types.Message, state:FSMContext):
    student_data['phone'] = message.text
    await message.answer("Введите ваш возраст")
    await state.set_state(Student.age)

@router.message(Student.age)
async def age(message:types.Message, state:FSMContext):
    student_data['age'] = message.text
    await message.answer("Введите свой класс")
    await state.set_state(Student.lesson)

