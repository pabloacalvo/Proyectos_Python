from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(   
            fg='white',
            bg='#000000',
            padx=40,
            pady=20,
            font=('Consolas',30)
            )
texto.pack()


texto = Label(ventana, text="Soy Pablo")
texto.config(
    width=400,
    height=4,
    bg='orange',
    font=('Arial',18),
    padx=10,
    pady=10,
    cursor = 'spider'
)
texto.pack(anchor=W)

def pruebas(nombre,apellido,pais):
    return f"Hola {nombre} {apellido} veo que sos de {pais}"


texto = Label(ventana, text= pruebas(pais='Argentina',nombre='Pablo',apellido='Calvo'))
texto.config(
    height=4,
    bg='yellow',
    font=('Arial',18),
    padx=10,
    pady=10,
    cursor = 'spider'
)
texto.pack(anchor=NW)

texto = Label(ventana, text="Master en Python")
texto.config(
    height=4,
    bg='yellow',
    font=('Arial',18),
    padx=10,
    pady=10,
    cursor = 'spider'
)
texto.pack(anchor=NW)

ventana.mainloop()