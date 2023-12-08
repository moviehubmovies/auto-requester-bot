import re
from pyrogram import Client, filters
from pyrogram.types import *
import os
import spotipy
import spotdl
import requests
import base64
from info import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

# just ignore this add the value in the info.py 
client_id = SPOTIFY_CLIENT_ID
client_secret = SPOTIFY_CLIENT_SECRET

# Encode the client id and client secret
credentials = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8')

# Define a function to get the access token
def get_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()['access_token']

async def download_and_upload_song(client, message, song_id):
    # Get the song's audio URL
    url = f'https://api.spotify.com/v1/tracks/{song_id}'
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    audio_url = data["preview_url"]

    # Use youtube-dl for better download options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality':
 
'192',
        }],
        'outtmpl': os.path.join("downloads", f"{song_id}.mp3")
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([audio_url])

    # Upload the audio file to Telegram
    await message.reply_audio(
        audio=os.path.join("downloads", f"{song_id}.mp3")
    )
    # Delete the downloaded audio file
    os.remove(os.path.join("downloads", f"{song_id}.mp3"))

@Client.on_message(filters.command("spotify"))
async def spotify(client, message):
    # Get the access token
    access_token = get_access_token()

    # Get the song name or Spotify URL from the command
    song_name_or_url = message.command[1:]
    song_name_or_url = " ".join(song_name_or_url)
    # Check if the command argument is a Spotify URL
    match = re.match(r'https://open\.spotify\.com/track/([a-zA-Z0-9]+)', song_name_or_url)
    if match:
        # If it is a Spotify URL, extract the song ID from the URL
        song_id = match.group(1)
    else:
        # If it is not a Spotify URL, search for the song on Spotify
        song_name = song_name_or_url
        url = f'https://api.spotify.com/v1/search?q={song_name}&type=album,track'
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        data = response.json()

        # Get the first search result
        item = data["tracks"]["items"][0]

        # Get the song ID
        song_id = item["id"]

    # Get the song thumbnail and details from Spotify
    url = f'https://api.spotify.com/v1/tracks/{song_id}'
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    # Get the song thumbnail
    thumbnail_url = data["album"]["images"][0]["url"]

    # Get the song details
    artist = data["artists"][0]["name"]
    name = data["name"]
    album = data["album"]["name"]
    release_date = data["album"]["release_date"]

    # Send the song thumbnail and details to the user
    await message.reply_photo(photo=thumbnail_url, caption=f"ʜᴇʏ {message.from_user.mention}\n\n ᴛɪᴛʟᴇ: <code>{name}</code>\nᴀʀᴛɪsᴛ: <code>{artist}</code>\nᴀʟʙᴜᴍ: <code>{album}</code>\nʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ: <code>{release_date}</code>\n")

    # Download the audio file
    download_options = {
        "format": "bestaudio/best",
        "output": os.path.join("downloads", f"{song_id}.mp3")
    }
    downloader = spotdl.Downloader(download_options)
    await downloader.download(audio_url)

    # Upload the audio file to Telegram
    await client.send_audio(
        chat_id=message.chat.id,
        audio=os.path.join("downloads", f"{song_id}.mp3")
    )

    # Delete the downloaded audio file
    os.remove(os.path.join("downloads", f"{song_id}.mp3"))
