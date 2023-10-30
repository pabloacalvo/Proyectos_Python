from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo('Alerta','Alerta!!')
    MessageBox.showerror('Error','ERROR')

def salir(nombre):
    resultado=MessageBox.askquestion('Salir','¿Continuar ejecutando la aplicacion')
    if resultado !='yes':
        MessageBox.showinfo('Chau!',f'Adios {nombre}')
        ventana.destroy()

Button(ventana, text='Mostras alerta!!!', command=sacarAlerta).pack()

Button(ventana, text='Salir', command=lambda :salir('Pablo Calvo')).pack()


ventana.mainloop()