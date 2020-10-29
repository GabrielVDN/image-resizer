import tkinter as tk
from tkinter import ttk
from frames.start_page import StartPage
from frames.download_page import DownloadPage
import tkinter.font as font
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


# Create a Tkinter Widget.
class ImageResizer(tk.Tk): 
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self)
        container.grid()

        # Set the style to 'clam'.
        style = ttk.Style()
        style.theme_use("clam")

        # Give the Widget a name.
        self.title("Image Resizer")
        # Give the Widget a size.
        self.geometry("400x200")
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 12 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=12)

        self.frames = {}
        for F in ():
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


GUI = ImageResizer()
GUI.mainloop()