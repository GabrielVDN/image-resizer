import tkinter as tk
from tkinter import ttk


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Add some labels.
        laberl1 = ttk.Label(self, text="Start Page")
        laberl1.grid()

        download_page_button = ttk.Button(
            self,
            text="Download Page",
            command=lambda: controller.show_frame("DownloadPage"),
        )
        download_page_button.grid(row=1, column=0, padx=12, pady=12, sticky="EW")
