import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Add some labels.
        laberl1 = ttk.Label(self, text="Start Page")
        laberl1.grid(row=0, column=0, padx=12, pady=12)

        button = ttk.Button(self, text='Open', command=self.UploadAction)
        button.grid(row=1, column=0, padx=12, pady=12, sticky="EW")

        download_page_button = ttk.Button(
            self,
            text="Download Page",
            command=lambda: controller.show_frame("DownloadPage"),
        )
        download_page_button.grid(row=2, column=0, padx=12, pady=12, sticky="EW")


    def UploadAction(event=None):
        filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("gif files", "*.gif*"), ("png files", "*.png")))
        print('Selected:', filename)