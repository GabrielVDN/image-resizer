import tkinter as tk
from tkinter import ttk
import time
import os
from tkinter import messagebox


PATH_APPDATA = os.getenv("APPDATA")

class ResizePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Add some widgets.
        label1 = ttk.Label(
            self, text="Chose the new size for the pictures.", font=('Verdana', 16)
        )
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
        radio1.grid(row=1, column=0, padx=12, pady=(15,8))
        
        radio2 = ttk.Radiobutton(
            self, text="20px", variable=controller.var_radio, value="20px"
        )
        radio2.grid(row=2, column=0, padx=12, pady=8)

        radio3 = ttk.Radiobutton(
            self, text="30px", variable=controller.var_radio, value="30px"
        )
        radio3.grid(row=3, column=0, padx=12, pady=8)

        radio4 = ttk.Radiobutton(
            self, text="40px", variable=controller.var_radio, value="40px"
        )
        radio4.grid(row=4, column=0, padx=12, pady=8)

        radio5 = ttk.Radiobutton(
            self, text="50px", variable=controller.var_radio, value="50px"
        )
        radio5.grid(row=5, column=0, padx=12, pady=8)

        radio6 = ttk.Radiobutton(
            self, text="60px", variable=controller.var_radio, value="60px"
        )
        radio6.grid(row=6, column=0, padx=12, pady=8)

        label2 = ttk.Label(self, font=('system', 12))
        label2.grid(row=7, column=0, padx=12, pady=(10,12))

        img_amount_done = tk.IntVar()
        
        progbar = ttk.Progressbar(
            self,
            orient=tk.HORIZONTAL, 
            mode='determinate',
            variable=img_amount_done,
            style="TProgressbar"
        )
        progbar.grid(row=8, column=0, padx=12, pady=12, sticky="EW")

        def resize_images():
            '''resize the chosen images'''
            if controller.var_radio.get() != '':
                img_amount = len(controller.all_img_paths)
                progbar['maximum'] = img_amount
                back_button['state'] = 'disabled'
                for img_path in controller.all_img_paths:
                    img_amount_done.set(img_amount_done.get()+1)
                    label2['text'] = f'Resizing: {img_amount_done.get()}/{img_amount}'
                    self.update()
                    time.sleep(0.5)

                label2['text'] = 'Done!'
                back_button['state'] = 'normal'
                img_amount_done.set(0)
                self.create_folder()
            else:
                messagebox.showerror("No Size Selected", "You need to select an image size!")


        resize_button = ttk.Button(
            self,
            text="Resize",
            command=resize_images
        )
        resize_button.grid(row=9, column=0, padx=12, pady=12, sticky="EW")

    def create_folder(self):
        with open(PATH_APPDATA+'\\image-resizer\\folder_count.txt', 'r') as outfile:
            folder_count = outfile.read()

        os.mkdir(f'C:\\resized-images-folder{folder_count}')
        with open(PATH_APPDATA+'\\image-resizer\\folder_count.txt', 'w') as outfile:
            outfile.write(str(int(folder_count)+1))
