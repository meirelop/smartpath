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
# bot = telebot.AsyncTeleBot(TOKEN)


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
    # bot.reply_to(message, HELLO)
    hello = 'Welcome to Traveler bot! \nI will help you acclimatize faster \n' \
            'Please select language...'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row('English')
    markup.row('Russian')
    markup.row('Kazakh')
    bot.send_message(message.chat.id, hello, reply_markup=markup)

@bot.message_handler(commands=['location'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    itembtn1 = types.KeyboardButton('Send location', request_location=True)
    markup.row(itembtn1)
    msg = 'Click button to share location'
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.message_handler(commands=['developer'])
def send_welcome(message):
    bot.reply_to(message, developer)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    audio_path = get_audio(message.voice.file_id)
    audio_text = voice.get_audio_text(audio_path)
    response = voice.getOutput(voice.getAnswer(audio_text))
    # bot.send_audio(message.chat.id, open(response, 'rb'))
    bot.send_voice(message.chat.id, open(response, 'rb'))

def choose_city(chatid):
    print 'choosecity'
    markup = types.ReplyKeyboardMarkup(True,True)
    markup.row('Astana')
    markup.row('Almaty')
    markup.row('Singapore')
    message = 'Select city'
    bot.send_message(chatid,message,markup)

@bot.message_handler(func=lambda message: message.text.lower() in ['english', 'russian', 'kazakh'])
def handle_language(message):
    message_text = message.text.lower()
    markup = types.ReplyKeyboardMarkup(True, True)
    markup.row('Astana')
    markup.row('Almaty')
    markup.row('Singapore')
    msg = 'Select city...'
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.message_handler(commands=['events'])
def handle_event(message):
    message_text = message.text.lower()
    markup = types.InlineKeyboardMarkup()
    message_reply = settings.EVENTS_BRIEF
    button_event1 = types.InlineKeyboardButton('1', url='http://telegra.ph/Events-04-19')
    button_event2 = types.InlineKeyboardButton('2', url='http://telegra.ph/Events-04-19')
    button_event3 = types.InlineKeyboardButton('3', url='http://telegra.ph/Events-04-19')
    markup.row(button_event1, button_event2, button_event3)
    bot.send_message(message.chat.id, message_reply, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == 'events')
def handle_event(message):
    message_text = message.text.lower()
    markup = types.InlineKeyboardMarkup()
    message_reply = settings.EVENTS_BRIEF
    button_event1 = types.InlineKeyboardButton('1', url='http://telegra.ph/Events-04-19')
    button_event2 = types.InlineKeyboardButton('2', url='http://telegra.ph/Events-04-19')
    button_event3 = types.InlineKeyboardButton('3', url='http://telegra.ph/Events-04-19')
    markup.row(button_event1, button_event2, button_event3)
    bot.send_message(message.chat.id, message_reply, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() in ['astana', 'almaty', 'singapore'])
def handle_city(message):
    message_text = message.text.lower()
    if message_text == 'singapore':
        msg = 'Please write your trip information for best result'
        bot.send_message(message.chat.id, msg)
        msg = 'Your flight number: '
        bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text.lower() == '701c')
def handle_location(message):
    msg = 'Please write your budget in $: '
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text == '4000')
def handle_location(message):
    msg = 'Please choose what kind of information do you prefer:  '
    markup = types.InlineKeyboardMarkup()
    button_event1 = types.InlineKeyboardButton('Food', url='http://telegra.ph/Events-04-19')
    button_event2 = types.InlineKeyboardButton('Sights', url='http://telegra.ph/Events-04-19')
    button_event3 = types.InlineKeyboardButton('Shopping', url='http://telegra.ph/Events-04-19')
    button_event4 = types.InlineKeyboardButton('Hang out', url='http://telegra.ph/Events-04-19')
    button_event5 = types.InlineKeyboardButton('All', url='http://telegra.ph/Events-04-19')
    markup.row(button_event1, button_event2, button_event3, button_event4, button_event5)
    bot.send_message(message.chat.id, msg, reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text.lower() in ['astana', 'almaty', 'singapore'])
# def handle_city(message):
#     message_text = message.text.lower()
#     if message_text == 'singapore':
#         msg = settings.SINGAPORE_ESSENTIALS
#         bot.send_message(message.chat.id, msg)
#         markup = types.ReplyKeyboardMarkup(True, True)
#         msg = 'How can I help you?'
#         button_take = types.KeyboardButton('From A to B')
#         button_location = types.KeyboardButton('Send Location', request_location=True)
#         button_essentials = types.KeyboardButton('Read Essentials')
#         button_another = types.KeyboardButton('Events')
#         markup.row(button_take, button_location)
#         markup.row(button_essentials, button_another)
#         bot.send_message(message.chat.id, msg, reply_markup=markup)

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
    if message_text == 'how do i use public transportation?':
        response = settings.BOT_ANSWER
    else:
        response = 'Could not understand'
    bot.send_message(message.chat.id, response)

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

