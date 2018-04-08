from settings import TOKEN, CHAT_ID
from messages import HELLO, developer
from telebot import types
import voice
import telebot
import requests
import subprocess
import string
import random
import os

bot = telebot.TeleBot(TOKEN)

def get_audio(file_id):
    filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    ogg_file = filename + '.ogg'
    wav_file = filename + '.wav'
    file_info = bot.get_file(file_id)
    response = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
    if response.status_code == 200:
        with open(ogg_file, 'wb') as f:
            for block in response.iter_content(1024):
                f.write(block)
        subprocess.call(['avconv', '-i', ogg_file, wav_file])
        os.remove(ogg_file)
    return wav_file


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, HELLO)

@bot.message_handler(commands=['developer'])
def send_welcome(message):
    bot.reply_to(message, developer)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    audio_path = get_audio(message.voice.file_id)
    audio_text = voice.get_audio_text(audio_path)
    # if audio_text.lower() in ['hello', 'hi']:
    #     print 'switched'
    response = voice.getOutput(voice.getAnswer(audio_text))
    bot.send_audio(message.chat.id, open(response, 'rb'))

@bot.message_handler(content_types=['text'])
def handle_text(message):
    response = 'temporary response'
    bot.send_message(message.chat.id, response)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling()