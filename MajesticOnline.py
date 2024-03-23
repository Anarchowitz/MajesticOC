import asyncio
import requests
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot('') # maded by dermaprojects
dp = Dispatcher(bot)

klava = ReplyKeyboardMarkup()
buttons = [
    '1. New York',
    '2. Detroit',
    '3. Chicago',
    '4. San Francisco',
    '5. Atlanta',
    '6. San Diego',
    '7. Los Angeles'
]
for button in buttons:
    klava.add(KeyboardButton(button))

@dp.message_handler(commands=['start'])
async def start_command(message):
    await message.answer(f"Привет, {message.chat.first_name}👋.\nMajesticOC\nПриятного использования\n(MajesticOnlineChecker)", reply_markup=klava)
def get_players(server):
    json = requests.get("https://api1master.majestic-files.com/meta/servers?region=ru").json()
    a = json["result"]["servers"][server - 1]["players"]
    return a
@dp.message_handler(text=buttons)
async def check_server(message):
    server_name = message.text.replace('. ', '')[1:]
    server_number = int(message.text.split('.')[0])
    players = get_players(server_number)
    if players > 2000:
        status = "✅"
    elif players < 10:
        status = "🛑"
    else:
        status = "✅"
    queue_message = "🕒 Возможна очередь!" if players > 2000 else ""
    await message.answer(f"Статус сервера {server_name} -> {status}\n🌐 Онлайн на сервере -> ({players})\n\n{queue_message}")
executor.start_polling(dp)
