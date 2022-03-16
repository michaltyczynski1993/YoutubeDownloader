from tkinter import *
import tkinter as tk
import ytdownloader as yt

class YtDownloaderGui(Frame):
    def __init__(self, master):
        super(YtDownloaderGui, self).__init__(master)
        self.pack(fill='both')
        self.create_widgets()

    def create_widgets(self):
        # creating labelframes for widgets
        self.stream_frame = LabelFrame(self,borderwidth=1, text='Single video/mp3')
        self.playlist_frame = LabelFrame(self, text='Playlist',borderwidth=1)
        
        # stream frame widgets
        self.lbl = Label(self.stream_frame, text = 'Enter video URL')
        self.user_input = Entry(self.stream_frame)
        self.download_button = Button(self.stream_frame, text='Download video')
        self.download_button['command'] = self.download_video
        self.complete_stream_text = Label(self.stream_frame, text='', fg='#11AD00')
        self.download_audio_bttn = Button(self.stream_frame, text='Download audio')
        self.download_audio_bttn['command'] = self.download_audio
        
        # playlist frame widgets
        self.playlist_lbl = Label(self.playlist_frame, text='Enter PlayList URL')
        self.playlist_entry = Entry(self.playlist_frame)
        self.playlist_download_bttn = Button(self.playlist_frame, text='Download all videos')
        self.playlist_download_bttn['command'] = self.download_video_playlist
        self.complete_playlist_text = Label(self.playlist_frame, text='', fg='#11AD00')
        self.playlist_audio_download = Button(self.playlist_frame, text='Download all audio')
        self.playlist_audio_download['command'] = self.download_audio_playlist
        
        # widgets positioning
        # stream frame
        self.stream_frame.pack(ipadx=20, ipady=20, fill='both', side='left', expand=True)
        self.playlist_frame.pack(ipadx=20, ipady=20, fill='both', side='left', expand=True)
        self.lbl.pack(padx='5', pady='2')
        self.user_input.pack(fill='x', padx='5')
        self.download_button.pack(fill='x', pady='5', padx='5')
        self.download_audio_bttn.pack(fill='x', padx='5')
        self.complete_stream_text.pack(side='bottom')
        
        # playlist frame
        self.playlist_lbl.pack(padx='5', pady='2')
        self.playlist_entry.pack(fill='x', padx='5')
        self.playlist_download_bttn.pack(fill='x', pady='5', padx='5')
        self.playlist_audio_download.pack(fill='x', padx='5')
        self.complete_playlist_text.pack(side='bottom')
    
    def download_video(self):
        url = self.user_input.get()
        if url == '':
            self.complete_stream_text['fg'] = '#BF271F'
            self.complete_stream_text['text'] = 'Enter URL to download video from YouTube.'
        yt.download_mp4(url)
        self.complete_stream_text['text'] = 'Download complete! Check Your folder.'
    
    def download_audio(self):
        url = self.user_input.get()
        if url == '':
            self.complete_stream_text['fg'] = '#BF271F'
            self.complete_stream_text['text'] = 'Enter URL to download audio from YouTube.'
        yt.download_mp3(url)
        self.complete_stream_text['text'] = 'Download complete! Check Your folder.'

    def download_video_playlist(self):
        url = self.playlist_entry.get()
        if url == '':
            self.complete_playlist_text['fg'] = '#BF271F'
            self.complete_playlist_text['text'] = 'Enter Playlist URL to download videos from YouTube.'
        yt.playlist_video_download(url)
        self.complete_playlist_text['text'] = 'Download complete! Check Your folder.'
    
    def download_audio_playlist(self):
        url = self.playlist_entry.get()
        if url == '':
            self.complete_playlist_text['fg'] = '#BF271F'
            self.complete_playlist_text['text'] = 'Enter Playlist URL to download audio from YouTube.'
        yt.playlist_mp3_download(url)
        self.complete_playlist_text['text'] = 'Download complete! Check Your folder.'
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Youtube downloader')
        self.geometry('700x200')


if __name__ == "__main__":
    app = App()
    YtDownloaderGui(app)
    app.mainloop()

