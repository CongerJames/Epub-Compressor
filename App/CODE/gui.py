import base64
import os
import tkinter as tk
from tkinter import filedialog, ttk
import runner2
import icon_base64

class MyWidget(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.path_selector = tk.Button(self, text='Select Folder', command=self.select_path, width=13)
        self.selected_path = tk.StringVar()
        self.path_entry = tk.Entry(self, textvariable=self.selected_path, width=60)

        self.number_selector_label = tk.Label(self, text='Compression (in %)')
        self.number_selector = tk.Scale(self, from_=10, to=50, orient='horizontal', length=370, resolution=5)
        self.number_selector.set(30)

        self.execute_button = tk.Button(self, text='Compress', command=self.execute_code, width=67)

        self.path_selector.grid(row=0, column=1, padx=1, pady=(5,0))
        self.path_entry.grid(row=0, column=2, padx=1, pady=1)
        self.number_selector_label.grid(row=1, column=1, padx= 1, pady=(15,0))
        self.number_selector.grid(row=1, column=2, padx=1, pady=1)
        self.execute_button.grid(row=3, column=1, columnspan=2, padx= 1, pady=15)

    def select_path(self):
        path = filedialog.askdirectory()
        self.selected_path.set(path)

    def execute_code(self):
        path = self.selected_path.get()
        number = self.number_selector.get()
        runner2.run_code(path,int(number))

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x130")
    root.resizable(False, False)
    root.wm_title("Epub Compressor")
    icon = icon_base64.icon_get()
    icondata= base64.b64decode(icon)
    tempFile= "icon.ico"
    iconfile= open(tempFile,"wb")
    iconfile.write(icondata)
    iconfile.close()
    root.wm_iconbitmap(tempFile)
    os.remove(tempFile)
    widget = MyWidget(root)
    widget.pack()
    root.mainloop()
