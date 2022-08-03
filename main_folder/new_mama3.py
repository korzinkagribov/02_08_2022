from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.geometry("150x200")

w = Label(root, text='GeeksForGeeks',
          font="50")

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack(side=RIGHT,
                fill=Y)

mylist = Listbox(root,
                 yscrollcommand=scroll_bar.set)

canvas = tkinter.Canvas(root, height=1200, width=1200)
canvas.config(scrollregion=canvas.bbox(ALL))
image = Image.open("D:\kuku.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.pack()

mylist.insert(END, photo)

#for line in range(1, 26):
    #mylist.insert(END, "Geeks " + str(line))

mylist.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=mylist.yview)

root.mainloop()