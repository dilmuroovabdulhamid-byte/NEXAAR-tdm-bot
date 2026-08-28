import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Siz bergan Bot Token va Admin Username
BOT_TOKEN = "8830746318:AAF2yOiZb4s0jTPO5LCkoVawTxpURpITMC0"
ADMIN_USERNAME = "@mirzhayev"

# GitHub Pages-dan olgan SSL havolangizni shu yerga qo'ying
WEB_APP_URL = "https://USERNAME.github.io/nexar-tdm-app/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 TDM Turnirlar (NEXAR)",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )
    await message.answer(
        f"🔥 **NEXAR ESPORTS** TDM Turnirlar botiga xush kelibsiz!\n\n"
        f"Turnirlarda qatnashish uchun pastdagi tugmani bosing.\n"
        f"👨‍💻 Admin: {ADMIN_USERNAME}",
        reply_markup=kb,
        parse_mode="Markdown"
    )

@dp.message(F.web_app_data)
async def handle_web_app_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    
    if data.get("action") == "register":
        tourney_name = data.get("tourney_name")
        user_id = message.from_user.id
        username = message.from_user.username or message.from_user.full_name

        await message.answer(
            f"✅ **Ro'yxatdan o'tdingiz!**\n\n"
            f"🏆 Turnir: **{tourney_name}**\n"
            f"👤 Ishtirokchi: @{username} (ID: `{user_id}`)\n\n"
            f"Administrator {ADMIN_USERNAME} siz bilan tez orada bog'lanadi.",
            parse_mode="Markdown"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
