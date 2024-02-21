import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from config import Token
from web_py import audio, audio1
from buttons import catalog
from turk_music_py import turk_audio
from arab_m import arab_f
from rus_m import russian

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Salom {message.from_user.full_name}", reply_markup=catalog)


@dp.callback_query(F.data == "uzbek")
async def callback_query(call: CallbackQuery):
    for i in audio:
        await call.message.answer_audio(audio=i)


@dp.callback_query(F.data == "turk")
async def callback_query(call: CallbackQuery):
    for i in turk_audio:
        await call.message.answer_audio(audio=i)


@dp.callback_query(F.data == "arab")
async def callback_query(call: CallbackQuery):
    for i in arab_f:
        await call.message.answer_audio(audio=i)


@dp.callback_query(F.data == "rus")
async def callback_query(call: CallbackQuery):
    for i in russian:
        await call.message.answer_audio(audio=i)


@dp.callback_query(F.data == "xor")
async def callback_query(call: CallbackQuery):
    for i in audio1:
        await call.message.answer_audio(audio=i)


async def main() -> None:
    bot = Bot(Token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
