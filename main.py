import tkinter as tk
from tkinter import ttk
from frames.start_page import StartPage
from frames.resize_page import ResizePage
import tkinter.font as font
import os
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


PATH_APPDATA = os.getenv("APPDATA")
# Check if the datafolder exist.
# If not, create it.
if not os.path.exists(PATH_APPDATA+'\\image-resizer'):
    os.mkdir(PATH_APPDATA+'\\image-resizer')

    with open(PATH_APPDATA+'\\image-resizer\\folder_count.txt', 'w') as outfile:
        outfile.write('1')

# Create a Tkinter Widget.
class ImageResizer(tk.Tk): 
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self)
        container.grid()

        # Set the style to 'clam'.
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TProgressbar", background='green')

        # Give the Widget a name.
        self.title("Image Resizer")
        # Give the Widget a size.
        self.geometry("820x580")
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 12 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=12)

        # Create the list in wich you'll save the selcted images.
        self.all_img_paths = []
        # Create all needed Variables.
        self.var_radio = tk.StringVar()


        self.frames = {}
        for F in (StartPage, ResizePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="NSEW")
    
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


GUI = ImageResizer()
GUI.mainloop()