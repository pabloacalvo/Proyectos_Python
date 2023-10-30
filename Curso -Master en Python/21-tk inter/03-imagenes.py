from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry('700x500')

Label(ventana,text = "Hola soy Pablo").pack(anchor=W)

imagen = Image.open('./Curso -Master en Python/21-tk inter/imagenes/lanus.png')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()