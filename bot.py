import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "8830746318:AAF2yOiZb4s0jTPO5LCkoVawTxpURpITMC0"
ADMIN_USERNAME = "@mirzhayev"
WEB_APP_URL = "https://dilmuroovabdulhamid-byte.github.io/NEXAAR.../"  # O'zingizning aniq havolangiz

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 NEXAR ESPORTS (Mini App)",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )
    await message.answer(
        f"🔥 **NEXAR ESPORTS** rasmiy botiga xush kelibsiz!\n\n"
        f"🏆 Turnirlar, tekin akkauntlar va UC xarid qilish uchun pastdagi tugmani bosing.\n\n"
        f"👨‍💻 Admin: {ADMIN_USERNAME}",
        reply_markup=kb,
        parse_mode="Markdown"
    )

@dp.message(F.web_app_data)
async def handle_web_app_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    action = data.get("action")
    details = data.get("details")
    user = message.from_user

    if action == "register_tdm_1v1":
        await message.answer(f"✅ **{details}** uchun arizangiz qabul qilindi.\nAdmin {ADMIN_USERNAME} tez orada siz bilan bog'lanadi.")
    
    elif action == "get_account":
        await message.answer(f"🎮 **{details}** so'rovingiz qabul qilindi.\nAkkaunt ma'lumotlarini olish uchun admin {ADMIN_USERNAME} ga yozing.")
        
    elif action == "topup_balance":
        await message.answer(f"💳 Hisob to'ldirish uchun to'lov rekvizitlarini {ADMIN_USERNAME} orqali oling.")
        
    elif action == "buy_uc":
        await message.answer(f"💎 **{details}** xarid qilish so'rovingiz yuborildi.\nAdmin {ADMIN_USERNAME} sizga to'lov va ID kiritish bo'yicha yo'riqnoma yuboradi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
