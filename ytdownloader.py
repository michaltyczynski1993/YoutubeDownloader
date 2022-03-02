from pytube import YouTube

def youTube_download(url):
    yt = YouTube(url)
    yt.title
    yt.streams.get_highest_resolution().download()

