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

API_ID = int(os.environ.get('API_ID', '8914119'))
API_HASH = os.environ.get('API_HASH', '652bae601b07c928b811bdb310fdb4b0')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '7135774957:AAGcLDtGkseQVcoaN5xxBel0I5Ht15kQWWk')
PORT = os.environ.get("PORT", "8080")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1342641151')]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002055184812'))

# for mongodb
DATABASE_NAME = os.environ.get("DB_NAME", "cBSSRccyjoHQMuAT")     
DATABASE_URI  = os.environ.get("DB_URL", "mongodb+srv://o53317853:cBSSRccyjoHQMuAT@cluster0.aerrmcs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MONGO_URL = os.environ.get('MONGO_URL', "")



