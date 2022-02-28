from tkinter import *

class YtDownloaderGui(Frame):
    def __init__(self, master):
        super(YtDownloaderGui, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass

root = Tk()
root.title('Youtube downloader')
root.geometry('300x250')
app = YtDownloaderGui(root)
root.mainloop()