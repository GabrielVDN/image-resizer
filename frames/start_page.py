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
        laberl1 = ttk.Label(self, text="Start Page", font=('bold', 25))
        laberl1.grid(row=0, column=0, padx=12, pady=12)

        img_listbox = tk.Listbox(self, height=10, width=60)
        img_listbox.grid(row=1, column=0, padx=12, pady=12)
        
        if not controller.all_img_paths:
            img_listbox.insert("end", "No imgages have been selcted")

        x = tk.IntVar()

        def get_imgages():
            '''open file explorer and let them select an imgage'''
            img_paths = list(filedialog.askopenfilenames(initialdir="\\Users\\gabri\\OneDrive\\Pictures\\SavedPictures", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("icon files", "*.ico"))))
            
            if img_paths:
                if len(img_paths) > 1:
                    print('+2')
                    for path in img_paths:
                        if path not in controller.all_img_paths:
                            controller.all_img_paths.append(path)
                else:
                    print('1')
                    if img_paths not in controller.all_img_paths:
                        controller.all_img_paths.append(img_paths)

            if x.get() == 1:
                img_listbox.delete(0,'end')

            if controller.all_img_paths:
                for img_path in controller.all_img_paths:
                    print(img_path)
                    if x.get() == 0:
                        img_listbox.delete(0, 'end')
                        x.set(1)

                    img_listbox.insert("end", img_path)

        button = ttk.Button(self, text='Import Some Pictures', command=get_imgages)
        button.grid(row=2, column=0, padx=12, pady=12, sticky="EW")

        download_page_button = ttk.Button(
            self,
            text="Next",
            command=lambda: controller.show_frame("DownloadPage"),
        )
        download_page_button.grid(row=3, column=0, padx=12, pady=12, sticky="EW")   
