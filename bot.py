import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Bot Token va Admin sozlamalari
BOT_TOKEN = "8830746318:AAF2yOiZb4s0jTPO5LCkoVawTxpURpITMC0"
ADMIN_USERNAME = "@mirzhayev"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
  kb = InlineKeyboardMarkup(
      inline_keyboard=[[
          InlineKeyboardButton(
              text="💬 Admin bilan bog'lanish",
              url=f"https://t.me/{ADMIN_USERNAME.replace('@', '')}",
          )
      ]]
  )

  await message.answer(
      f"Salom, <b>{message.from_user.first_name}</b>!\n\n"
      "🔥 <b>NEXAR ESPORTS</b> rasmiy botiga xush kelibsiz.\n\n"
      "🏆 Turnirlarda qatnashish, tekin akkauntlar va UC xarid qilish uchun"
      " pastdagi <b>Mini App</b> tugmasini bosing!\n\n"
      f"👨‍💻 Admin: {ADMIN_USERNAME}",
      reply_markup=kb,
      parse_mode="HTML",
  )


async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  asyncio.run(main())
