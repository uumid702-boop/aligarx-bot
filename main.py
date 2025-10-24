main.pyfrom aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "BU_YERGA_OZINGNING_BOT_TOKENINGNI_KIRIT"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("👋 Salom! Bu Aligarx Token tizimiga ulangan botning test versiyasi.\n\nTez orada token olish, balansni ko‘rish va boshqa funksiyalar qo‘shiladi.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
