from aiogram import Router
from aiogram.types import Message
import sqlite3
from AI.AI import handle_conversation
from aiogram.filters import Command
import datetime
from os.path import isfile

router = Router()

context1 = " "


def ftime():
    return str(datetime.datetime.now().time())[:8]


@router.message(Command("erasecontext"))
async def erase_history_of_user(message: Message):
    global context1
    context1 = " "
    await message.reply("Work in progress....")


@router.message(Command("context"))
async def send_context(message: Message):
    global context1
    try:
        if len(context1) > 1024:
            for x in range(0, len(context1), 1024):
                await message.reply(context1[x : x + 1024])
    except:
        await message.reply("No context")


@router.message()
async def communication(message: Message):
    global context1

    if not isfile("context_data.db"):
        open("context_data.db", "+w").close()

    connection = sqlite3.connect("context_data.db")
    cursor = connection.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Chats (
    chat_id INTEGER NOT NULL,
    context TEXT NOT NULL,
    )
    """
    )

    try:
        print(f"Processing request - {ftime()}")
        reply, context2 = handle_conversation(message.text, context1)

        if len(reply) > 1024:
            for x in range(0, len(reply), 1024):
                await message.reply(reply[x : x + 1024])
        else:
            await message.reply(reply)
        context1 = context2
        print(f"Processed - {ftime()}\n")
    except UnboundLocalError:
        print(f"unbound error - {ftime()}")
        reply, context2 = handle_conversation(message.text, "")
        await message.reply(reply)
        context1 = context2
    except Exception as Exc:
        print(f"{Exc} - {ftime()}")
