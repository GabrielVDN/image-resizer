import tkinter as tk
from tkinter import ttk
import time


class DownloadPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Add some widgets.
        label1 = ttk.Label(self, text="Chose the new size for the pictures.", font=('Verdana', 20))
        label1.grid(row=0, column=0, padx=12, pady=12)
        
        back_button = ttk.Button(
            self,
            text="🔙",
            width=3,
            command=lambda: controller.show_frame("StartPage"),
        )
        back_button.grid(row=0, column=0, padx=12, pady=12, sticky="E")

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

        label2 = ttk.Label(self, font=('system', 15))
        label2.grid(row=5, column=0, padx=12, pady=(30, 12))

        int_var = tk.IntVar()
        progbar = ttk.Progressbar(
            self,
            orient=tk.HORIZONTAL, 
            mode='determinate',
            maximum=100,
            variable=int_var,
            style="TProgressbar"
        )
        progbar.grid(row=6, column=0, padx=12, pady=12, sticky="EW")

        def add1():
            print(f"resizing in to {controller.var_radio.get()}")
            label2['text'] = 'Resizing'
            back_button['state'] = 'disabled'
            while int_var.get() < 101:
                int_var.set(int_var.get()+1)
                time.sleep(0.01)
                self.update()
            label2['text'] = 'Done!'
            self.update()
            time.sleep(1)
            int_var.set(0)

        resize_button = ttk.Button(
            self,
            text="Resize",
            command=add1
        )
        resize_button.grid(row=7, column=0, padx=12, pady=12, sticky="EW")
