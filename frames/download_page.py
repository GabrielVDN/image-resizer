import tkinter as tk
from tkinter import ttk


class DownloadPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Add some labels.
        laberl1 = ttk.Label(self, text="Chose the new size for the pictures.", font=('Verdana', 20))
        laberl1.grid(row=0, column=0, padx=12, pady=12)
        
        start_page_button = ttk.Button(
            self,
            text="🔙",
            width=3,
            command=lambda: controller.show_frame("StartPage"),
        )
        start_page_button.grid(row=0, column=0, padx=12, pady=12, sticky="E")

        radio1 = ttk.Radiobutton(
            self, text="10px", variable=controller.var_radio, value="10px"
        )
        radio1.grid(row=1, column=0, padx=12, pady=12)
        
        radio2 = ttk.Radiobutton(
            self, text="20px", variable=controller.var_radio, value="20px"
        )
        radio2.grid(row=2, column=0, padx=12, pady=12)

        radio3 = ttk.Radiobutton(
            self, text="30px", variable=controller.var_radio, value="30px"
        )
        radio3.grid(row=3, column=0, padx=12, pady=12)

        radio4 = ttk.Radiobutton(
            self, text="40px", variable=controller.var_radio, value="40px"
        )
        radio4.grid(row=4, column=0, padx=12, pady=12)
        
        start_page_button = ttk.Button(
            self,
            text="Resize",
            command=lambda: print(f"resizing in to {controller.var_radio.get()}")
        )
        start_page_button.grid(row=5, column=0, padx=12, pady=12, sticky="EW")
