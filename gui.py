from tkinter import *
import tkinter as tk
from turtle import color
import ytdownloader as yt

class YtDownloaderGui(Frame):
    def __init__(self, master):
        super(YtDownloaderGui, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text = 'Enter video URL')
        self.user_input = Entry(self)
        self.download_button = Button(self, text='Download')
        self.download_button['command'] = self.download
        self.complete_lbl = Label(self, text='', fg='#11AD00')
        
        # widgets positioning
        self.lbl.grid(column = 0, row = 0,pady=5)
        self.user_input.grid(column = 0, row = 1, pady=5)
        self.download_button.grid(row=2, pady=5)
        self.complete_lbl.grid(row=3)
    
    def download(self):
        url = self.user_input.get()
        if url == '':
            self.complete_lbl['fg'] = '#BF271F'
            self.complete_lbl['text'] = 'Enter URL to download video from YouTube.'
        yt.youTube_download(url)
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

