# -*- coding: utf-8 -*-
import settings
from settings import *
from messages import *
from buttons import *
from telebot import types
import telebot
import time
from datetime import datetime
import voice
import requests
import subprocess
import string
import random
import os

# bot = telebot.TeleBot(TOKEN)
bot = telebot.AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print 'bot started'
    bot.send_message(message.chat.id, msg_hello)
    markup = types.ReplyKeyboardMarkup(True, True)
    markup.row(btn_language, rbtn_language)
    bot.send_message(message.chat.id, msg_language, reply_markup=markup)

@bot.message_handler(commands=['shrug'])
def send_welcome(message):
    bot.send_message(message.chat.id, msg_shrug)

@bot.message_handler(func=lambda message: message.text.lower() == u'🇷🇺 русский')
def russian_handler(message):
    bot.send_message(message.chat.id, rmsg_action, reply_markup=r_main_markup)

@bot.message_handler(func=lambda message: message.text.lower() == u'🇬🇧 english')
def english_handler(message):
    bot.send_message(message.chat.id, msg_action, reply_markup=main_markup)


@bot.message_handler(func = lambda message: message.text.lower() == u'🎁 мероприятия')
def r_events(message):
    print '%s entered' % message.text.lower
    event = ru_events[1]
    markup = types.InlineKeyboardMarkup()
    button_right = types.InlineKeyboardButton(btn_next, callback_data='ru_2')
    button_left = types.InlineKeyboardButton(btn_prev, callback_data='ru_0')
    button_url = types.InlineKeyboardButton(rbtn_inline_full, url=ru_event_urls[1])
    markup.row(button_left, button_right, button_url)
    bot.send_message(message.chat.id, event, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == u'🎁 events')
def handle_event(message):
    print '%s entered' % message.text.lower
    event = en_events[1]
    markup = types.InlineKeyboardMarkup()
    button_right = types.InlineKeyboardButton(btn_next, callback_data='en_2')
    button_left = types.InlineKeyboardButton(btn_prev, callback_data='en_0')
    button_url = types.InlineKeyboardButton(btn_inline_full, url=en_event_urls[1])
    markup.row(button_left, button_right, button_url)
    bot.send_message(message.chat.id, event, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() == u'❓ ask question')
def handle_event(message):
    bot.send_message(message.chat.id, msg_question)

@bot.message_handler(func=lambda message: message.text.lower() == u'❓ задать вопрос')
def handle_event(message):
    bot.send_message(message.chat.id, rmsg_question)


@bot.message_handler(func=lambda message: message.text.lower() == u'🆘 tips and tricks')
def handle_event(message):
    print '%s entered' % message.text.lower
    markup = types.ReplyKeyboardMarkup(True, True)
    markup.row(btn_emergency, btn_currency)
    markup.row(btn_weather, btn_back)
    bot.send_message(message.chat.id, msg_action, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == u'🆘 советы и подсказки')
def handle_event(message):
    print '%s entered' % message.text.lower
    markup = types.ReplyKeyboardMarkup(True, True)
    markup.row(r_btn_emergency, r_btn_currency)
    markup.row(r_btn_weather, r_btn_back)
    bot.send_message(message.chat.id, rmsg_action, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() == u'🔙 go back')
def handle_event(message):
    bot.send_message(message.chat.id, msg_action, reply_markup=main_markup)

@bot.message_handler(func=lambda message: message.text.lower() == u'🔙 назад')
def handle_event(message):
    bot.send_message(message.chat.id, rmsg_action, reply_markup=r_main_markup)

@bot.message_handler(func=lambda message: message.text.lower() == u'☎️ emergency')
def handle_event(message):
    bot.send_message(message.chat.id, url_emergency)

@bot.message_handler(func=lambda message: message.text.lower() == u'☎️ экстренные номера')
def handle_event(message):
    bot.send_message(message.chat.id, ru_url_emergency)

@bot.message_handler(func=lambda message: message.text.lower() == u'💱 currency')
def handle_event(message):
    bot.send_message(message.chat.id, url_currency)
    bot.send_message(message.chat.id, msq_currencies)

@bot.message_handler(func=lambda message: message.text.lower() == u'💱 валюта')
def handle_event(message):
    bot.send_message(message.chat.id, ru_url_currency)
    bot.send_message(message.chat.id, ru_msg_currencies)

@bot.message_handler(func=lambda message: message.text.lower() in [u'🌐 change language', u'🌐 сменить язык'])
def handle_event(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    markup.row(btn_language, rbtn_language)
    bot.send_message(message.chat.id, msg_language, reply_markup=markup)


@bot.callback_query_handler(func=lambda query: True)
def hande_query(query):
    try:
        markup = types.InlineKeyboardMarkup()
        language = query.data[:2]
        event_num = int(query.data[3:])
        if event_num > 6 or event_num < 1:
            bot.answer_callback_query(query.id, btn_end)
        if language == 'en':
            next_event = en_events[event_num]
            button_url = types.InlineKeyboardButton(btn_inline_full, url=en_event_urls[event_num])
        else:
            next_event = ru_events[event_num]
            button_url = types.InlineKeyboardButton(rbtn_inline_full, url=ru_event_urls[event_num])
        callback_next = '%s_%s' % (language, str(event_num + 1))
        callback_prev = '%s_%s' % (language, str(event_num - 1))
        button_right = types.InlineKeyboardButton(btn_next, callback_data=callback_next)
        button_left = types.InlineKeyboardButton(btn_prev, callback_data=callback_prev)
        markup.row(button_left, button_right, button_url)
        bot.edit_message_text(next_event,query.message.chat.id,query.message.message_id,reply_markup=markup)
    except Exception as e:
        print e
        pass

@bot.message_handler(content_types=['text'])
def handle_text(message):
    message_text = str(message.text.lower())
    print message_text
    for key in redis_keys:
        key = unicode(key, 'utf-8')
        if key in message_text:
            answer = redis_con.get(key)
        else:
            answer = msg_shrug
    bot.send_message(message.chat.id, answer)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print message
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print 'Error in main: %s' %e
            time.sleep(10)