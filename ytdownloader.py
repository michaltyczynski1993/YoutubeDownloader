from pytube import YouTube
from pytube import Playlist

def download_mp4(url):
    yt = YouTube(url)
    yt.title
    yt.streams.get_highest_resolution().download()

def download_mp3(url):
    yt = YouTube(url)
    yt.title
    yt.streams.get_audio_only().download()

def playlist_video_download(playlist_url):
    playlist = Playlist(playlist_url)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download()

def playlist_mp3_download(playlist_url):
    playlist = Playlist(playlist_url)
    for video in playlist.videos:
        video.streams.get_audio_only().download()