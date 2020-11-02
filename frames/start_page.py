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

        def UploadAction(event=None):
            filename = filedialog.askopenfilename(initialdir="\\Users\\gabri\\OneDrive\\Pictures\\SavedPictures", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("gif files", "*.gif*"), ("png files", "*.png")))

            image_label = ttk.Label(self, text=filename)
            image_label.grid(row=3, column=0, padx=12, pady=12)
            
            my_image = ImageTk.PhotoImage(Image.open(filename))
            my_image_label = ttk.Label(self, image=my_image)
            my_image_label.grid(row=4, column=0, padx=12, pady=12)

        # Add some labels.
        laberl1 = ttk.Label(self, text="Start Page")
        laberl1.grid(row=0, column=0, padx=12, pady=12)

        button = ttk.Button(self, text='Open', command=UploadAction)
        button.grid(row=1, column=0, padx=12, pady=12, sticky="EW")

        download_page_button = ttk.Button(
            self,
            text="Download Page",
            command=lambda: controller.show_frame("DownloadPage"),
        )
        download_page_button.grid(row=2, column=0, padx=12, pady=12, sticky="EW")
