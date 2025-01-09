from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from app.states import Student, student_data

router = Router()

@router.message(Command("start"))
async def start(message:types.Message, state:FSMContext):
    student_data['chat_id'] = message.text
    await message.answer("Привет я бот для учате ваших занятий. Напишите свое имя!")
    await state.set_state(Student.name)