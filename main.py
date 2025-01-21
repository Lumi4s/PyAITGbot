from aiogram import Bot, Dispatcher
import asyncio
import wmi
from os import kill
import signal

from app.handlers import ftime
from app.handlers import router
from bot_token import bot_token


async def main():
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print(f"-----------------\nstart - {ftime()}\n")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        deleter = wmi.WMI()
        for process in deleter.Win32_Process(name="ollama_llama_server.exe"):
            kill(process.ProcessId, signal.SIGTERM)
        print(f"off - {ftime()}\n-----------------")
