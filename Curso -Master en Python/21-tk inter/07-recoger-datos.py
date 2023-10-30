from tkinter import *


def getDato():
    resultado.set(dato.get())
    if len(resultado.get()) >=1:
        texto_recogido.config(
    bg = 'green',
    fg = 'white'
)


ventana = Tk()
ventana.geometry('700x700')
ventana.config(
        bd=50,
        )
dato = StringVar()
resultado = StringVar()
Label(ventana, text="Ingresa un texto").pack(side=LEFT, anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text='Dato recodigo ').pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.pack(anchor=NW)

Button(ventana, text='Mostrar dato', command=getDato).pack(anchor=NW)



ventana.mainloop()