from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk

ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#5F734C')

frame = Frame(
    ws,
    bg='#A8B9BF'
    )

text_box = Text(
    ws,
    height=13,
    width=32,
    font=(12)
)

text_box.grid(row=0, column=0)
text_box.config(bg='#D9D8D7')

sb = Scrollbar(
    ws,
    orient=VERTICAL
    )

sb.grid(row=1, column=0, sticky=NS)

canvas = tkinter.Canvas(ws, height=1200, width=1200)
image = Image.open("D:\kuku.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(row=2, column=1)

ws.mainloop()