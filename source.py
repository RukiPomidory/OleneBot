import telebot
import config
import requests
import re
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['Занятия'])
def lesson(message):
    response = requests.get(config.site)
    res = re.search(r'Занятия.+<br', str(response.text))
    bot.send_message(message.chat.id, res.group(0)[0:-3])


@bot.message_handler(commands=['test'])
def test(message):
    response = requests.get(config.site)
    bot.send_message(message.chat.id, response.text)


if __name__ == '__main__':
    bot.polling()
