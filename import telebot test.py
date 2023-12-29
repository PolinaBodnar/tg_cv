# !pip install pytelegrambotapi
import telebot
from telebot import types
# Токен вашего бота
bot = telebot.TeleBot(token='6781457349:AAGp82R5O6hzgrw8hoavMG4OMLtbbRieD0c', parse_mode='html')
recommendations = {
    'Текст': 'Бот для составления текста: https://t.me/gigachat_bot',
    'Изображения': 'Бот для генерации изображений: https://t.me/gigachat_bot',
    'Музыка': 'Бот для создания музыки: https://t.me/gigachat_bot',
    'Код': 'Бот валидатор кода: https://t.me/gigachat_bot'
}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который поможет найти чаты нейросети для редактирования текста, изображений, музыки и кода. Введите /recommend_text, /recommend_images, /recommend_music или /recommend_code для получения ссылок.")

# Обработчики команд с рекомендациями
@bot.message_handler(commands=['recommend_text'])
def send_text_recommendation(message):
    recommendation = recommendations.get('текст', 'Рекомендация для с текстом.')
    bot.reply_to(message, recommendation)

@bot.message_handler(commands=['recommend_images'])
def send_images_recommendation(message):
    recommendation = recommendations.get('изображения', 'Рекомендация для работы с изображением.')
    bot.reply_to(message, recommendation)

@bot.message_handler(commands=['recommend_music'])
def send_music_recommendation(message):
    recommendation = recommendations.get('музыка', 'Рекомендация для работы с музыкой.')
    bot.reply_to(message, recommendation)

@bot.message_handler(commands=['recommend_code'])
def send_code_recommendation(message):
    recommendation = recommendations.get('код', 'Рекомендация для работы кодом.')
    bot.reply_to(message, recommendation)
