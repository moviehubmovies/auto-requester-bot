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
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
REQUESTED_CHANNEL = int(os.environ.get("REQUESTED_CHANNEL", ""))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
ADMIN_CHANNEL_ID = int(os.environ.get("ADMIN_CHANNEL_ID", ""))
EVAL_ID = int(os.environ.get("EVAL_ID", ""))

# clone bots
LOG_CHANNEL_INFORM = int(os.environ.get("LOG_CHANNEL_INFORM", ""))
LOG_CHANNEL_ERROR = int(os.environ.get("LOG_CHANNEL_ERROR", ""))

# important information for your bot
S_GROUP = environ.get('S_GROUP', "https://t.me/sdbots_support")
S_CHANNEL = environ.get('S_CHANNEL', "https://t.me/sd_bots")

#sample
#F_SUB = os.environ.get("FORCE_SUB", "sd_bots") 
F_SUB = os.environ.get("FORCE_SUB", "") 


# for mongodb
DATABASE_NAME = os.environ.get("DB_NAME", "")     
DATABASE_URI  = os.environ.get("DB_URL", "")
MONGO_URL = os.environ.get('MONGO_URL', "")

#for spotify 
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID', 'd3a0f15a75014999945b5628dca40d0a')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET', 'e39d1705e35c47e6a0baf50ff3bb587f')

#for google
G_API_KEY = os.environ.get('G_API_KEY','AIzaSyAGv5kIu2-E0N9eTdK7lzevl2nr3sOk6is')


