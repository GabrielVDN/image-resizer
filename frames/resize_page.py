import tkinter as tk
from tkinter import ttk
import time
import os
from tkinter import messagebox
from PIL import Image


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
            self, text="Instagram Square Photo", variable=controller.var_radio, value=1
        )
        radio1.grid(row=1, column=0, padx=(250, 0), pady=(15,8), sticky="W")
        
        radio2 = ttk.Radiobutton(
            self, text="Instagram Landscape Photo", variable=controller.var_radio, value=2
        )
        radio2.grid(row=2, column=0, padx=(250, 0), pady=8, sticky="W")

        radio3 = ttk.Radiobutton(
            self, text="Instagram Portrait Photo", variable=controller.var_radio, value=3
        )
        radio3.grid(row=3, column=0, padx=(250, 0), pady=8, sticky="W")

        radio4 = ttk.Radiobutton(
            self, text="Square Image", variable=controller.var_radio, value=4
        )
        radio4.grid(row=4, column=0, padx=(250, 0), pady=8, sticky="W")

        radio5 = ttk.Radiobutton(
            self, text="Half The Original Size", variable=controller.var_radio, value=5
        )
        radio5.grid(row=5, column=0, padx=(250, 0), pady=8, sticky="W")

        label2 = ttk.Label(self, font=('system', 12))
        label2.grid(row=7, column=0, padx=12, pady=(26,12))

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
                resize_button['state'] = 'disabled'
                create_folder()
                for img_path in controller.all_img_paths:
                    img_amount_done.set(img_amount_done.get()+1)
                    label2['text'] = f'Resizing: {img_amount_done.get()}/{img_amount}'
                    self.update()

                    resize_image(img_path)

                    time.sleep(0.2)

                label2['text'] = 'Done!'
                self.update()
                time.sleep(1)
                back_button['state'] = 'normal'
                resize_button['state'] = 'normal'
                img_amount_done.set(0)
                label2['text'] = 'All the images are stored in a folder in C:\\'
            else:
                messagebox.showerror("No Size Selected", "You need to select an image size!")

        def resize_image(img_path):
            im = Image.open(img_path)
            if controller.var_radio.get() == 1:
                im = im.resize((1080, 1080),Image.ANTIALIAS)

            elif controller.var_radio.get() == 2:
                im = im.resize((1080, 608),Image.ANTIALIAS)

            elif controller.var_radio.get() == 3:
                im = im.resize((1080, 1350),Image.ANTIALIAS)

            elif controller.var_radio.get() == 4:
                im = im.resize((400, 400),Image.ANTIALIAS)

            elif controller.var_radio.get() == 5:
                h, w = im.size
                im = im.resize((int(h/2),int(w/2)),Image.ANTIALIAS)

            img = img_path.split('/')
            im = im.save(f'C:\\resized-images-folder{controller.folder_count.get()}\\{img[-1]}')


        resize_button = ttk.Button(
            self,
            text="Resize",
            command=resize_images
        )
        resize_button.grid(row=9, column=0, padx=12, pady=12, sticky="EW")

        def create_folder():
            '''create a folder in C:\ and store all resized images'''
            with open(PATH_APPDATA+'\\image-resizer\\folder_count.txt', 'r') as outfile:
                f_c = outfile.read()

            controller.folder_count.set(f_c)
            

            os.mkdir(f'C:\\resized-images-folder{controller.folder_count.get()}')

            with open(PATH_APPDATA+'\\image-resizer\\folder_count.txt', 'w') as outfile:
                outfile.write(str(int(controller.folder_count.get())+1))
