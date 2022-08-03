import main_note as m

m.main_dunction()
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
root = Tk()
frm = ttk.Frame(root, padding = 10)
frm.grid()
ttk.Label(frm, text ="Hello World!").grid (column = 0, row = 0)
ttk.Label(frm, text ="Каталог с картинками").grid (column = 7, row = 7)
canvas = tkinter.Canvas(root, height=1200, width=1200)
image = Image.open("D:\kuku.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.grid(row=2,column=1)
root.mainloop()
ttk.Button(frm, text ="Quit", command=root.destroy).grid (column = 1, row = 0)
root.mainloop()

class App(tkinter):
    def __init__(self):
        super().__init__()
        self.scroll_x = tkinter.Scrollbar(self, orient=tkinter.HORIZONTAL)
        self.scroll_y = tkinter.Scrollbar(self, orient=tkinter.VERTICAL)
        self.canvas = tkinter.Canvas(self, width=300, height=100,
                                xscrollcommand=self.scroll_x.set,
                                yscrollcommand=self.scroll_y.set)
        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)

        self.frame = tkinter.Frame(self.canvas)
        self.btn = tkinter.Button(self.frame, text="Загрузить изображение",
                             command=self.load_image)
        self.btn.pack()

        self.canvas.create_window((0, 0), window=self.frame,
                                  anchor=tkinter.N + tkinter.W)

        self.canvas.grid(row=0, column=0, sticky="nswe")
        self.scroll_x.grid(row=1, column=0, sticky="we")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.bind("", self.resize)
        self.update_idletasks()
        self.minsize(self.winfo_width(), self.winfo_height())

    def resize(self, event):
        region = self.canvas.bbox(tkinter.ALL)
        self.canvas.configure(scrollregion=region)

    def load_image(self):
        self.btn.destroy()
        self.image = tkinter.PhotoImage(file="D:\kuku.jpg")
        tkinter.Label(self.frame, image=self.image).pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()