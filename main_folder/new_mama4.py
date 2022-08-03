from tkinter import *
from PIL import Image, ImageTk
import tkinter

root = Tk() #Создание окна

frame = Frame(root, bd=2, relief=SUNKEN) #Создание контейнеров верхнего уровня, тут распологаются - bd как ширина границ и relief - стиль рельефа

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1) # определение размера строк в сетке grid

xscrollbar = Scrollbar(frame, orient=HORIZONTAL) #Определение ориентации с применением перемнной Frame
xscrollbar.grid(row=1, column=0, sticky=E+W) #Определение элемента сетки с указанием положения и ориентацией относительно компаса east west. Создание скролла по вертикали

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)# Определение элемента сетки (скролла) и определение в y-оси

canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)# Применение к рамке ширины границ, свойств скролла
canvas.grid(row=0, column=0, sticky=N+S+E+W)# Расположение рамки по компасу

File = "D:\kuku.jpg"
img = ImageTk.PhotoImage(Image.open(File))#Создание виджета изображения для использования в аргументах методов и функций
canvas.create_image(0, 0, image=img, anchor="nw")#Создание изображение в выделенной области с ориентацией по компасу
canvas.config(scrollregion=canvas.bbox(ALL))#Применение метода конфигураций с использованием выделения области по "рамке",

xscrollbar.config(command=canvas.xview)#установление регулировки при изменении по x
yscrollbar.config(command=canvas.yview)#установление регулировки при изменении по y

frame.pack() #Запаковка ячейки верхнего уровня
root.mainloop()


#http://epydoc.sourceforge.net/stdlib/Tkinter.Canvas-class.html - canvas functions