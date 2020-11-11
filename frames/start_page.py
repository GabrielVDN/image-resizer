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
        laber1 = ttk.Label(self, text="Image Resizer", font=('Verdana', 35))
        laber1.grid(rowspan=2, column=0, padx=12, pady=12)

        img_listbox = tk.Listbox(self, height=10, width=60)
        img_listbox.grid(row=2, columnspan=3, padx=12, pady=12)
        
        img_listbox.insert("end", "No images have been selcted.")

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

        btn_get_img = ttk.Button(
            self, text='Import Some Pictures', command=lambda: [get_imgs(), next_btn()]
        )
        btn_get_img.grid(row=0, column=1, padx=12, pady=12, sticky="EW")

        def delete_img():
            '''Delete selection from listbox'''
            selection = img_listbox.curselection()
            try:
                img_listbox.delete(selection[0])
                controller.all_img_paths.pop(selection[0])
            except:
                pass
            if len(controller.all_img_paths) == 0 and not img_listbox.get(0):
                img_listbox.insert("end", "No images have been selcted.")

        def next_btn():
            if len(controller.all_img_paths) > 0:
                next_page_button['state'] = 'normal'
                next_page_button['text'] = 'Next'
            else:
                next_page_button['state'] = 'disabled'
                next_page_button['text'] = 'First select images/an image'

        btn_delete_img = ttk.Button(
            self, text='Delete Selected Picture', command=lambda: [delete_img(), next_btn()]
        )
        btn_delete_img.grid(row=1, column=1, padx=12, pady=12, sticky="EW")

        next_page_button = ttk.Button(
            self,
            text="First select images/an image",
            command=lambda: controller.show_frame("DownloadPage"),
            state="disabled"
        )
        next_page_button.grid(row=3, columnspan=3, padx=12, pady=12, sticky="EW")  
