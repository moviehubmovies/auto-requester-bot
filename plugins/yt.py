from pyrogram import Client, filters
from yt_dlp import YoutubeDL


@Client.on_message(filters.command("yt"))
async def youtube_to_audio(client, message):
    # Extract YouTube link from message
    video_url = message.text.split()[1]

    # Download audio using yt_dlp with preferred codec and quality
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        # Extract info and prepare filename
        info = ydl.extract_info(video_url, download=False)
        audio_file = ydl.prepare_filename(info)

        # Download audio data directly
        with open(audio_file, "wb") as file:
            ydl.process_video(video_url, download=False, callback=lambda data: file.write(data))

    # Extract artist and thumbnail (optional)
    artist = info.get("artist")
    thumbnail_url = info["thumbnails"][0]["url"] if info["thumbnails"] else None

    # Send downloaded audio directly with info
    await message.reply_audio(
        audio_file=audio_file,
        title=info["title"],
        duration=info["duration"],
        performer=artist,
        thumb=thumbnail_url,
    )

    # Delete temporary audio file
    os.remove(audio_file)
