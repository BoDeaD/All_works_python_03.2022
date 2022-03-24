'''
Задание 3
'''
from telebot import TeleBot

TOKEN = '1691000503:AAFm7v_4JL47LZ6yxywq3DHODjw1UzDbj1I'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['/start'])
def start_message(message):
 bot.send_message(message.chat.id,'Приветик')
@bot.message_handler(content_types=['Приветик'])
def send_text(message):
 if message.text == ' How are you?   ':
  bot.send_message(message.chat.id, 'I am fine today, thank you for question!')
bot.polling()