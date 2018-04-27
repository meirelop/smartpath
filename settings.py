# -*- coding: utf-8 -*-
import os
import redis
redis_con = redis.StrictRedis('127.0.0.1', 6379, db=8)
redis_keys = redis_con.keys('*')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_ROOT = os.path.join(BASE_DIR, 'images')

#BOT TOKEN
TOKEN = '428302944:AAFYGDhIPxTaPa1vJtlODRksGGUWU8QH6Uk'

#CHAT_ID = '262839968'  # blacksteak
GOOGLE_PLACES_API = 'AIzaSyCbCeTWSqRfBsolOQdMl3GMJAAG6lK-Mso'

# AWS CREDENTIALS
ACCESS_KEY = 'AKIAJDCIF6JQTTL755YQ'
SECRET_KEY = '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'
BUCKET = 'iotrecognitionbucket'

# Additional
SINGAPORE_ESSENTIALS = 'http://telegra.ph/Traveller-Essentials-in-Singapore-04-19'
