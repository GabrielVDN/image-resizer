import tkinter as tk
from tkinter import ttk


class DownloadPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Add some labels.
        laberl1 = ttk.Label(self, text="Download Page")
        laberl1.grid(row=0, column=0, padx=12, pady=12)
        
        start_page_button = ttk.Button(
            self,
            text="Start Page",
            command=lambda: controller.show_frame("StartPage"),
        )
        start_page_button.grid(row=1, column=0, padx=12, pady=12, sticky="S")
