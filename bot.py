import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "7219089727:AAHeBZLZ2GMYj_JUGhkGjcA11l19OE9kSbc"

dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message) -> None:
    await message.answer("Бот готов приступить к работу!")
    
    
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())     