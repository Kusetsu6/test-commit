import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "8589645001:AAElRXcd-wb-6omGsANKEDp5mTMmzEcANGo"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Звичайні кнопки (ReplyKeyboard) ---
reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📌 Інформація")],
        [KeyboardButton(text="🌐 Сайт")]
    ],
    resize_keyboard=True
)

# --- Inline кнопки ---
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔗 Відкрити Google", url="https://google.com")],
        [InlineKeyboardButton(text="Натисни мене", callback_data="btn_click")]
    ]
)

# Команда старт
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привіт! Обери кнопку 👇", reply_markup=reply_kb)

# Обробка звичайних кнопок
@dp.message()
async def handle_message(message: types.Message):
    if message.text == "📌 Інформація":
        await message.answer("Це тестовий бот 🤖", reply_markup=inline_kb)
    elif message.text == "🌐 Сайт":
        await message.answer("Ось посилання:", reply_markup=inline_kb)

# Обробка inline кнопки
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "btn_click":
        await callback.message.answer("Ти натиснув inline кнопку ✅")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())