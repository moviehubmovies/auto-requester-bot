import os
from pyrogram.errors import ChatAdminRequired , FloodWait
import random
import asyncio
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from pyrogram import enums , filters , Client
from info import API_ID , API_HASH , BOT_TOKEN , PORT , ADMINS , LOG_CHANNEL , DATABASE_NAME , DATABASE_URI
from Script import script
import time
from utils import temp , get_size
from pyrogram.errors import FloodWait
from database.users_db import db
import re
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client , message):
    if message.chat.type in [enums.ChatType.GROUP , enums.ChatType.SUPERGROUP]:
        button = [[InlineKeyboardButton("🔸 MAIN CHANNEL 1 🔸" , url="https://t.me/+S5EJw3_afjq88XPK")
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(text=script.START_TXT.format(message.from_user.mention , temp.U_NAME , temp.B_NAME) ,
                            reply_markup=reply_markup)
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id , message.from_user.first_name)
        await client.send_message(LOG_CHANNEL ,
                                  script.LOG_TEXT_P.format(message.from_user.id , message.from_user.mention ,
                                                           message.from_user.id))
    if len(message.command) != 2:
            mine = await client.get_me()
            button = [[InlineKeyboardButton("🔸 MAIN CHANNEL 1 🔸" , url="https://t.me/+S5EJw3_afjq88XPK")
                  ]]
            await client.send_message(chat_id=message.chat.id ,
                                      text=f"__Hello {message.from_user.mention} Iam Auto Approver Join Request Bot Just [Add Me To Your Group or Channnl](http://t.me/{mine.username}?startgroup=botstart)__" ,
                                      reply_markup=InlineKeyboardMarkup(button) , disable_web_page_preview=True)
