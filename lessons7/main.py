import aioschedule as schedule
import asyncio

async def task():
    print("Задача Выполняется")

async def hello():
    print("Hello World")

async def start():
    schedule.every(1).second.do(task)
    schedule.every(1).second.do(hello)

    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

asyncio.run(start())