import yt_dlp

url = input("Enter YouTube URL: ")

options = {
    "format": "bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s",
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])