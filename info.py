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

API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
PORT = os.environ.get("PORT", "8080")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '')]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))

# for mongodb
DATABASE_NAME = os.environ.get("DB_NAME", "")     
DATABASE_URI  = os.environ.get("DB_URL", "")
MONGO_URL = os.environ.get('MONGO_URL', "")



