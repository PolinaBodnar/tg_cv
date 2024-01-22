#библиотеки, которые загружаем из вне

import telebot
import logging

TOKEN = '6497731850:AAETqU3_FfB94FYFbWRiB2Tkxkuy_8GQcVY'

from telebot import types

# создание объекта TeleBot
bot = telebot.TeleBot(TOKEN)

# блок для логирования ошибок
logging.basicConfig(filename='bot.log', level=logging.ERROR)

try:
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
except Exception as e:
    logging.error(f"Ошибка при отправке стикера: {e}")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🧡 Мое портфолио")
    item2 = types.KeyboardButton("🧡 Мой репозиторий")
    item3 = types.KeyboardButton("😋 Написать мне в личку")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет тебе от It-семьи, {0.first_name}!".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

# назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🧡 Мое портфолио':
            bot.send_message(message.chat.id, 'https://www.behance.net/PaolaBodnar')
        elif message.text == '😋 Написать мне в личку':
            bot.send_message(message.chat.id, 'https://t.me/paolabodnar')
        elif message.text == '🧡 Мой репозиторий':
            bot.send_message(message.chat.id, 'https://github.com/PolinaBodnar')
        else:
            bot.send_message(message.chat.id, 'Не знаю что ответить😢')

# запуск бота
bot.polling(none_stop=True)
