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

        # Add some labels.
        laberl = ttk.Label(self, text="Start Page", font=('Verdana', 50))
        laberl.grid(rowspan=2, column=0, padx=12, pady=12)

        img_listbox = tk.Listbox(self, height=10, width=60)
        img_listbox.grid(row=2, columnspan=3, padx=12, pady=12)
        
        img_listbox.insert("end", "No imgages have been selcted")

        x = tk.IntVar()

        def get_imgs():
            '''open file explorer and let them select an imgage'''
            img_paths = list(filedialog.askopenfilenames(initialdir="\\Users\\gabri\\OneDrive\\Pictures\\SavedPictures", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("icon files", "*.ico"))))
            
            if img_paths:
                for path in img_paths:
                    if path not in controller.all_img_paths:
                        controller.all_img_paths.append(path)

            if x.get() == 1:
                img_listbox.delete(0,'end')

            if controller.all_img_paths:
                for img_path in controller.all_img_paths:
                    if x.get() == 0:
                        img_listbox.delete(0, 'end')
                        x.set(1)

                    img_listbox.insert("end", img_path)

        btn_get_img = ttk.Button(self, text='Import Some Pictures', command=get_imgs)
        btn_get_img.grid(row=0, column=1, padx=12, pady=12, sticky="EW")

        def delete_img():
            '''Delete selection from listbox'''
            selection = img_listbox.curselection()
            try:
                print(selection)
                img_listbox.delete(selection[0])
            except:
                pass

        btn_delete_img = ttk.Button(self, text='Delete Selected Picture', command=delete_img)
        btn_delete_img.grid(row=1, column=1, padx=12, pady=12, sticky="EW")

        download_page_button = ttk.Button(
            self,
            text="Next",
            command=lambda: controller.show_frame("DownloadPage"),
        )
        download_page_button.grid(row=3, columnspan=3, padx=12, pady=12, sticky="EW")   
