# -*- coding: utf-8 -*-
import telebot
from telebot import types


btn_end = "That's all"

btn_inline_full = 'ℹ️ Full info'
rbtn_inline_full = 'ℹ️ Подробнее'
btn_next = '➡️'
btn_prev = '⬅️'

btn_events = '🎁 Events'
btn_tips = '🆘 Tips and tricks'
btn_qa = '❓ Ask question'
btn_change = '🌐 Change language'

rbtn_events = '🎁 Мероприятия'
rbtn_tips = '🆘 Советы и подсказки'
rbtn_qa = '❓ Задать вопрос'
rbtn_change = '🌐 Сменить язык'

btn_language = '🇬🇧 English'
rbtn_language = '🇷🇺 Русский'

# tips buttons
btn_currency = '💱 Currency'
btn_weather = '🌡️ Weather'
btn_emergency = '☎️ Emergency'
btn_back = '🔙 Go back'

r_btn_currency = '💱 Валюта'
r_btn_weather = '🌡️ Погода'
r_btn_emergency = '☎️ Экстренные номера'
r_btn_back = '🔙 Назад'


main_markup = types.ReplyKeyboardMarkup(True, True)
main_markup.row(btn_events, btn_tips)
main_markup.row(btn_qa, btn_change)

r_main_markup = types.ReplyKeyboardMarkup(True, True)
r_main_markup.row(rbtn_events, rbtn_tips)
r_main_markup.row(rbtn_qa, rbtn_change)