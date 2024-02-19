from pyrogram import Client, filters
import requests
import os

@Client.on_message(filters.command("pic"))
async def download(client, message):
 try:
    url = message.text.split()[1]
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open('image.JPEG', 'wb') as f:
            f.write(response.content)

        await message.reply_photo(photo='image.JPEG')
        os.remove('image.JPEG')
    else:
        await message.reply_text('Failed to download image.')
 except Exception as e:
        await message.reply_text(f"{e}")

@Client.on_message(filters.command("video"))
async def download(client, message):
    try:
        url = message.text.split()[1]
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open('video.mp4', 'wb') as f:
                f.write(response.content)
            await message.reply_video(video='video.mp4')
            os.remove('video.mp4')
        else:
            await message.reply_text('Failed to download video.')
    except Exception as e:
        await message.reply_text(f"{e}")

@Client.on_message(filters.command("imagine"))
async def imagine(client, message):
 try:
    width = 500
    height = 500
    url = f"https://picsum.photos/{width}/{height}"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open('image.jpg', 'wb') as f:
            f.write(response.content)

        await message.reply_photo(photo='image.jpg')
    else:
        await message.reply_text('Failed to generate image.')
 except Exception as e:
        await message.reply_text(f"{e}")

