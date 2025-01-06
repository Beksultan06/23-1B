from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("about"))
async def about(message:types.Message):
    await message.answer("Информация о нас")

