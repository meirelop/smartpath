# -*- coding: utf-8 -*-
import settings
from settings import TOKEN
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

@bot.message_handler(commands=['start'])
def send_welcome(message):
    hello = 'Welcome to Travel Assistant bot! \nI will help you acclimatize faster \n' \
            'Please select your target location...'
    bot.send_message(message.chat.id, hello)
    markup = types.ReplyKeyboardMarkup(True, True)
    markup.row('Astana')
    markup.row('Almaty')
    markup.row('Singapore')
    msg = 'Select city...'
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.message_handler(commands=['location'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    itembtn1 = types.KeyboardButton('Send location', request_location=True)
    markup.row(itembtn1)
    msg = 'Click button to share location'
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    print("{0}, {1}".format(message.location.latitude, message.location.longitude))
    bot.send_message(message.chat.id, 'location handled')

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    audio_path = get_audio(message.voice.file_id)
    audio_text = voice.get_audio_text(audio_path)
    response = voice.getOutput(voice.getAnswer(audio_text))
    bot.send_voice(message.chat.id, open(response, 'rb'))

@bot.message_handler(func=lambda message: message.text.lower() in ['events', '/events'])
def handle_event(message):
    markup = types.InlineKeyboardMarkup()
    message_reply = settings.EVENTS_BRIEF
    button_event1 = types.InlineKeyboardButton('1', url=settings.URL_LAGMAN)
    button_event2 = types.InlineKeyboardButton('2', url=settings.URL_KOREAN)
    button_event3 = types.InlineKeyboardButton('3', url=settings.URL_3)
    button_event4 = types.InlineKeyboardButton('4', url=settings.URL_BALET)
    button_event5 = types.InlineKeyboardButton('4', url=settings.URL_WINE)
    markup.row(button_event1, button_event2, button_event3, button_event4, button_event5)
    bot.send_message(message.chat.id, message_reply, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == 'singapore')
def handle_city(message):
    msg = settings.SINGAPORE_ESSENTIALS
    bot.send_message(message.chat.id, msg)
    markup = types.ReplyKeyboardMarkup(True, True)
    msg = 'How can I help you?'
    button_take = types.KeyboardButton('From A to B')
    button_location = types.KeyboardButton('Send Location', request_location=True)
    button_essentials = types.KeyboardButton('Read Essentials')
    button_another = types.KeyboardButton('Events')
    markup.row(button_take, button_location)
    markup.row(button_essentials, button_another)
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == 'send location')
def handle_location(message):
    print message
    # bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text.lower() == 'read essentials')
def handle_essentials(message):
    msg = settings.SINGAPORE_ESSENTIALS
    bot.send_message(message.chat.id, msg)
    markup = types.ReplyKeyboardMarkup(True, True)
    msg = 'How can I help you?'
    button_take = types.KeyboardButton('From A to B')
    button_location = types.KeyboardButton('Send Location', request_location=True)
    button_essentials = types.KeyboardButton('Read Essentials')
    button_another = types.KeyboardButton('Events')
    markup.row(button_take, button_location)
    markup.row(button_essentials, button_another)
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    message_text = message.text.lower()
    print message_text

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print message
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['photo'])
def photo(message):
    message = message.from_user
    photo_file = bot.get_file(message.photo[-1].file_id)
    photo_file.download('user_photo.jpg')


if __name__ == '__main__':
    bot.polling()

