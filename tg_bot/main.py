import telebot
import requests 
from telebot import types
from aiogram import bot



TOKEN = '6097729590:AAFFOTdxIeU2ksew9Hkr4iA_5SMespgM70g'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['wheather'])
def weather(message):
    url = 'https://wttr.in'
    weather_parameters = {
        '0' : '', #Текущая погода
        'T' : '', #Тихая версия
        'lang': 'ru' #Язык
    }

    responce = requests.get(url,params=weather_parameters)
    bot.send_message(message.chat.id, responce.text)


@bot.message_handler(commands=['but'])
def command(message):
    markup = types.InlineKeyboardMarkup()
    my_btn = types.InlineKeyboardButton(text = 'моя страничка', url = 'https://t.me/Trololoshka228_BrawlStarser2013')
    markup.add(my_btn)
    bot.send_message(message.chat.id, 'нажми меня', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def talk_bot(message):
    if message.text == 'привет': 
         bot.send_message(message.chat.id, 'Привет') 
    elif message.text == 'как дела':
        bot.send_message(message.chat.id, 'нормуль, у тебя?')
    elif message.text == 'тоже норм':
        bot.send_message(message.chat.id, 'ну оки')
    else: 
        bot.send_message(message.chat.id, message.text)



    


bot.polling()