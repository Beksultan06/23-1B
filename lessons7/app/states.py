from aiogram.fsm.state import State, StatesGroup

class Student(StatesGroup):
    name = State()
    phone = State()
    age = State()
    lesson = State()
    task = State()
    deadline = State()

student_data = {}