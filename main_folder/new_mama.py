import tkinter as tk
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
class Scrollbar_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("petuch")

        self.scrollbar = tk.Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(self.window, yscrollcommand=self.scrollbar.set)

        for i in range(100):
            self.listbox.insert("end", str(i))
        self.listbox.pack(side="left", fill="both")

        self.scrollbar.config(command=self.listbox.yview)

        self.window.mainloop()

        self.canvas = tkinter.Canvas(self.window, height=1200, width=1200)
        self.image = Image.open("D:\kuku.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)



if __name__ == '__main__':
    app = Scrollbar_Example()