from cgitb import text
from tkinter import *
import tkinter as tk
from turtle import left
import ytdownloader as yt

class YtDownloaderGui(Frame):
    def __init__(self, master):
        super(YtDownloaderGui, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # creating labelframes for widgets
        self.stream_frame = LabelFrame(self,borderwidth=1, text='Single video/mp3')
        self.playlist_frame = LabelFrame(self, text='Playlist',borderwidth=1)
        # stream frame widgets
        self.lbl = Label(self.stream_frame, text = 'Enter video URL')
        self.user_input = Entry(self.stream_frame)
        self.download_button = Button(self.stream_frame, text='Download')
        self.download_button['command'] = self.download_video
        self.complete_lbl = Label(self, text='', fg='#11AD00')
        # playlist frame widgets
        self.playlist_lbl = Label(self.playlist_frame, text='Enter PlayList URL')
        self.playlist_entry = Entry(self.playlist_frame)
        self.playlist_download_bttn = Button(self.playlist_frame, text='Download all videos')
        self.playlist_audio_download = Button(self.playlist_frame, text='Download all audio')
        
        # widgets positioning
        # stream frame
        self.stream_frame.pack(ipadx=20, ipady=20, fill='x', side='left', expand=True)
        self.playlist_frame.pack(ipadx=20, ipady=20, fill='x', side='left', expand=True)
        self.lbl.pack()
        self.user_input.pack()
        self.download_button.pack()
        self.complete_lbl.pack()
        # playlist frame
        self.playlist_lbl.pack()
        self.playlist_entry.pack()
        self.playlist_download_bttn.pack(fill='x')
        self.playlist_audio_download.pack(fill='x')
    
    def download_video(self):
        url = self.user_input.get()
        if url == '':
            self.complete_lbl['fg'] = '#BF271F'
            self.complete_lbl['text'] = 'Enter URL to download video from YouTube.'
        yt.download_mp4(url)
        self.complete_lbl['text'] = 'Download complete! Check Your folder.'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Youtube downloader')
        self.geometry('400x200')


if __name__ == "__main__":
    app = App()
    YtDownloaderGui(app)
    app.mainloop()

