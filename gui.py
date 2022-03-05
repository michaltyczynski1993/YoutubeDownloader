from tkinter import *
import tkinter as tk
import ytdownloader as yt

class YtDownloaderGui(Frame):
    def __init__(self, master):
        super(YtDownloaderGui, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.stream_frame = LabelFrame(self,borderwidth=1)
        self.playlist_frame = LabelFrame(self, text='Playlist',borderwidth=1)
        self.lbl = Label(self.stream_frame, text = 'Enter video URL')
        self.user_input = Entry(self.stream_frame)
        self.download_button = Button(self.stream_frame, text='Download')
        self.download_button['command'] = self.download_video
        self.complete_lbl = Label(self, text='', fg='#11AD00')
        
        # widgets positioning
        self.stream_frame.grid(column=0, row=0)
        self.playlist_frame.grid(column=1, row=0)
        self.lbl.grid(column = 0, row = 0,pady=5)
        self.user_input.grid(column = 0, row = 1, pady=5)
        self.download_button.grid(row=2, pady=5)
        self.complete_lbl.grid(row=3)
    
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
        self.geometry('300x300')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = App()
    YtDownloaderGui(app)
    app.mainloop()

