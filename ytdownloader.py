from pytube import YouTube

url = 'https://www.youtube.com/watch?v=Js1oQoyLeig'
yt = YouTube(url)
yt.title
yt.streams.get_highest_resolution().download()
print('Download Success!')