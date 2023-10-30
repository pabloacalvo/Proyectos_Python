"""
Calculadora:
- con dos campos de texto
- botones para las operaciones
- mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()
ventana.title('Ejercicio completo con TkInter')
ventana.geometry('400x400')
ventana.config(
    bd=25)

def setFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        MessageBox.showerror('Error','Introduce datos correctos')
    return result

def sumar():
    
    resultado.set(setFloat(numero1.get()) + setFloat(numero2.get()))
    mostrar_resultado()
   
        
def restar():
    resultado.set(setFloat(numero1.get()) - setFloat(numero2.get()))
    mostrar_resultado()

def multiplicar():
    resultado.set(setFloat(numero1.get()) * setFloat(numero2.get()))
    mostrar_resultado()

def dividir():
    if float(numero2.get()) == 0:
        MessageBox.showerror('Error','No se puede dividir entre cero')
    else:
        resultado.set(setFloat(numero1.get()) / setFloat(numero2.get()))
        mostrar_resultado()

def mostrar_resultado():
    MessageBox.showinfo('Resultado',f'El resultado de la operacion es {resultado.get()}')
    numero1.set('')
    numero2.set('')

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd = 5,
    relief=SOLID

)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)


Label(marco, text='Primer numero: ').pack()
Entry(marco, textvariable=numero1, justify='center').pack()

Label(marco, text='Segundo numero: ').pack()
Entry(marco, textvariable=numero2,justify='center').pack()

Label(marco, text='').pack()

Button(marco, text='SUMAR', command=sumar).pack(side='left', fill=X, expand=YES)
Button(marco, text='RESTAR', command=restar).pack(side='left', fill=X, expand=YES)
Button(marco, text='MULTIPLICAR', command=multiplicar).pack(side='left', fill=X, expand=YES)
Button(marco, text='DIVIDIR', command=dividir).pack(side='left', fill=X, expand=YES)




















ventana.mainloop()