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
    bot.send_message(message.chat.id, res[0:-3])


if __name__ == '__main__':
    bot.polling()
