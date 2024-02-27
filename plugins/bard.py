from pyrogram import Client, filters

text="```python\nimport pyrogram\nfrom pyrogram import filters\nfrom pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup\nfrom pytube import YouTube\n\nAPI_ID = 123456\nAPI_HASH = '0123456789abcdef0123456789abcdef'\n\nbot = pyrogram.Client('my_bot', api_id=API_ID, api_hash=API_HASH)\n\n\n@bot.on_message(filters.command(['start']))\ndef start(client, message):\n    keyboard = [\n        [\n            InlineKeyboardButton('Download YouTube Video', callback_data='download_video')\n        ]\n    ]\n\n    reply_markup = InlineKeyboardMarkup(keyboard)\n\n    message.reply_text('Hi! I can help you download videos from YouTube.', reply_markup=reply_markup)\n\n\n@bot.on_callback_query(filters.regex('download_video'))\ndef download_video(client, callback_query):\n    message = callback_query.message\n\n    message.reply_text('Send me the YouTube video URL:')\n\n\n@bot.on_message(filters.regex('(https?://)?(www\\.)?youtube\\.com/.*'))\ndef download_video_url(client, message):\n    video_url = message.text\n\n    try:\n        yt = YouTube(video_url)\n    except:\n        message.reply_text('Invalid YouTube video URL.')\n        return\n\n    video_title = yt.title\n    video_streams = yt.streams.filter(progressive=True, file_extension='mp4')\n\n    keyboard = []\n    for stream in video_streams:\n        video_quality = str(stream.resolution) + 'p'\n        video_size = str(round(stream.filesize / (1024 * 1024), 2)) + ' MB'\n        keyboard.append([InlineKeyboardButton(f'{video_quality} ({video_size})', callback_data=f'download_{stream.itag}')])\n\n    reply_markup = InlineKeyboardMarkup(keyboard)\n\n    message.reply_text(f'<b>{video_title}</b>\\n\\nSelect the video quality to download:', reply_markup=reply_markup)\n\n\n@bot.on_callback_query(filters.regex('download_(.*)'))\ndef download_video_quality(client, callback_query):\n    itag = callback_query.data.split('_')[1]\n\n    message = callback_query.message\n    chat_id = message.chat.id\n\n    try:\n        video_url = message.text.split('\\n')[0]\n        yt = YouTube(video_url)\n        stream = yt.streams.get_by_itag(itag)\n        stream.download(output_path=f'{chat_id}/{stream.default_filename}')\n    except:\n        message.reply_text('Error downloading video.')\n        return\n\n    message.reply_document(f'{chat_id}/{stream.default_filename}', caption=f'<b>{stream.default_filename}</b>')\n\n\nbot.run()\n```\n\nTo use this bot, you need to create a Telegram bot and get its API ID and API Hash. You can then replace the `API_ID` and `API_HASH` variables in the code with your bot's API ID and API Hash.\n\nYou can also customize the bot's behavior by modifying the `start()` and `download_video_url()` functions. For example, you could add additional features such as the ability to download videos in different formats or to convert videos to audio files."
message="```python\nimport pyrogram\nfrom pyrogram import filters\nfrom pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup\nfrom pytube import YouTube\n\nAPI_ID = 123456\nAPI_HASH = '0123456789abcdef0123456789abcdef'\n\nbot = pyrogram.Client('my_bot', api_id=API_ID, api_hash=API_HASH)\n\n\n@bot.on_message(filters.command(['start']))\ndef start(client, message):\n    keyboard = [\n        [\n            InlineKeyboardButton('Download YouTube Video', callback_data='download_video')\n        ]\n    ]\n\n    reply_markup = InlineKeyboardMarkup(keyboard)\n\n    message.reply_text('Hi! I can help you download videos from YouTube.', reply_markup=reply_markup)\n\n\n@bot.on_callback_query(filters.regex('download_video'))\ndef download_video(client, callback_query):\n    message = callback_query.message\n\n    message.reply_text('Send me the YouTube video URL:')\n\n\n@bot.on_message(filters.regex('(https?://)?(www\\.)?youtube\\.com/.*'))\ndef download_video_url(client, message):\n    video_url = message.text\n\n    try:\n        yt = YouTube(video_url)\n    except:\n        message.reply_text('Invalid YouTube video URL.')\n        return\n\n    video_title = yt.title\n    video_streams = yt.streams.filter(progressive=True, file_extension='mp4')\n\n    keyboard = []\n    for stream in video_streams:\n        video_quality = str(stream.resolution) + 'p'\n        video_size = str(round(stream.filesize / (1024 * 1024), 2)) + ' MB'\n        keyboard.append([InlineKeyboardButton(f'{video_quality} ({video_size})', callback_data=f'download_{stream.itag}')])\n\n    reply_markup = InlineKeyboardMarkup(keyboard)\n\n    message.reply_text(f'<b>{video_title}</b>\\n\\nSelect the video quality to download:', reply_markup=reply_markup)\n\n\n@bot.on_callback_query(filters.regex('download_(.*)'))\ndef download_video_quality(client, callback_query):\n    itag = callback_query.data.split('_')[1]\n\n    message = callback_query.message\n    chat_id = message.chat.id\n\n    try:\n        video_url = message.text.split('\\n')[0]\n        yt = YouTube(video_url)\n        stream = yt.streams.get_by_itag(itag)\n        stream.download(output_path=f'{chat_id}/{stream.default_filename}')\n    except:\n        message.reply_text('Error downloading video.')\n        return\n\n    message.reply_document(f'{chat_id}/{stream.default_filename}', caption=f'<b>{stream.default_filename}</b>')\n\n\nbot.run()\n```\n\nTo use this bot, you need to create a Telegram bot and get its API ID and API Hash. You can then replace the `API_ID` and `API_HASH` variables in the code with your bot's API ID and API Hash.\n\nYou can also customize the bot's behavior by modifying the `start()` and `download_video_url()` functions. For example, you could add additional features such as the ability to download videos in different formats or to convert videos to audio files.",

@Client.on_message(filters.command("hi"))
async def hi(client, message):
    await message.reply_text(text)
    await message.reply_text(message)
