from aiogram.fsm.state import State, StatesGroup

class Student(StatesGroup):
    name = State()
    age = State()
    phone = State()
    lesson = State()
    task = State()
    deadline = State()

student_data = {}