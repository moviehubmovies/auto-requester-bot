import re
import os
from os import environ
from pyrogram import enums
import asyncio
import json
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

API_ID = int(os.environ.get('API_ID', '7679954'))
API_HASH = os.environ.get('API_HASH', '4af51af8f1a8b06ca2b076370ba93fba')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '1447478080:AAESvxi-7JjMSkWsGv2WdHLMX-u7lwgBp1k')
PORT = os.environ.get("PORT", "8080")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2144812475')]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002239864052'))

# for mongodb
DATABASE_NAME = os.environ.get("DB_NAME", "newbot")     
DATABASE_URI  = os.environ.get("DB_URL", "mongodb+srv://newbot:newbot@cluster0.hybkhvr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MONGO_URL = os.environ.get('MONGO_URL', "")



