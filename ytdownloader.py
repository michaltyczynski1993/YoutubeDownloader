from pytube import YouTube

def download_mp4(url):
    yt = YouTube(url)
    yt.title
    yt.streams.get_highest_resolution().download()

def download_mp3(url):
    yt = YouTube(url)
    yt.title
    yt.streams.get_audio_only().download()
