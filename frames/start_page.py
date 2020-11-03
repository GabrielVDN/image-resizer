import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Store the already selected files in a list.
        filenamelist = []

        # Add some labels.
        laberl1 = ttk.Label(self, text="Start Page")
        laberl1.grid(row=0, column=0, padx=12, pady=12)

        img_listbox = tk.Listbox(self, height=10, width=60)
        img_listbox.grid(row=1, column=0, padx=12, pady=12)
        
        

        def get_imgages():
            '''open file explorer and let them select an imgage'''
            filename = filedialog.askopenfilename(initialdir="\\Users\\gabri\\OneDrive\\Pictures\\SavedPictures", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("icon files", "*.ico")))
            if filename and filename not in filenamelist:
                img_listbox.insert("end", filename)
                filenamelist.append(filename)

        button = ttk.Button(self, text='Open', command=get_imgages)
        button.grid(row=2, column=0, padx=12, pady=12, sticky="EW")

        download_page_button = ttk.Button(
            self,
            text="Download Page",
            command=lambda: controller.show_frame("DownloadPage"),
        )
        download_page_button.grid(row=3, column=0, padx=12, pady=12, sticky="EW")   
